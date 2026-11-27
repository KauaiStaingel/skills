#!/usr/bin/env python3
"""Heuristic source scan for repeated generated-UI defaults.

The scan is evidence for review, not a design verdict. Visual structure, hierarchy,
content fit, and product specificity still require a rendered inspection.

Usage:
  python3 audit_ui.py <file-or-directory> [...]
  python3 audit_ui.py --json <paths...>
  python3 audit_ui.py --strict <paths...>
  python3 audit_ui.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SOURCE_EXTENSIONS = {
    ".astro", ".css", ".html", ".htm", ".js", ".jsx", ".mdx",
    ".scss", ".svelte", ".ts", ".tsx", ".vue",
}
SKIP_DIRECTORIES = {
    ".git", ".next", ".venv", "build", "coverage", "dist",
    "node_modules", "out", "vendor",
}
IGNORE_MARKER = "ui-developer-ignore:"


@dataclass(frozen=True)
class Rule:
    code: str
    level: str
    description: str
    pattern: re.Pattern[str]


def rule(code: str, level: str, description: str, pattern: str) -> Rule:
    return Rule(code, level, description, re.compile(pattern, re.IGNORECASE))


RULES = (
    rule("A1", "strong", "eyebrow or overline treatment", r"\b(eyebrow|kicker|overline|section-label)\b|uppercase[^\n]{0,100}tracking-(?:wide|wider|widest)"),
    rule("A2", "strong", "gradient-clipped text", r"bg-clip-text|background-clip\s*:\s*text|-webkit-text-fill-color\s*:\s*transparent"),
    rule("A3", "strong", "accent-colored phrase inside a primary heading", r"<h[12][^>]*>[^\n]{0,500}<span[^>]*(?:text-(?:primary|accent|brand|indigo|violet|purple|blue|green|orange|rose)|color\s*:)[^>]*>"),
    rule("A4", "review", "common display-serif escape; verify brief and cluster", r"\b(?:Playfair Display|Instrument Serif|DM Serif Display|Fraunces|Cormorant|Newsreader)\b"),
    rule("A5", "strong", "colored side or top stripe on a card", r"border-(?:l|t)-(?:4|\[3px\]|\[4px\])\b|border-(?:left|top)\s*:\s*[3-4]px\s+solid|border-inline-start\s*:\s*[3-4]px"),
    rule("A7", "strong", "pulsing attention cue", r"animate-(?:ping|pulse)|@keyframes\s+(?:ping|pulse|blink)\b"),
    rule("A8", "strong", "sparkle or AI badge", r"\bSparkles\b|lucide-sparkles|powered by ai|ai-powered|feito com ia"),
    rule("A9", "review", "emoji used in source; verify whether it is an icon", r"[\U0001F300-\U0001FAFF✨⭐⚡]"),
    rule("A10", "review", "Tailwind-like purple or indigo default", r"\b(?:indigo|violet|purple|fuchsia)-(?:400|500|600|700)\b|#(?:6366f1|7c3aed|8b5cf6|a855f7)\b"),
    rule("A11", "review", "small numbered circle; verify whether the process is real", r"rounded-full[^\n>]{0,150}(?:w|h|size)-(?:8|9|10|11|12)[^>]*>\s*(?:0?[1-9])\s*<"),
    rule("A12", "review", "glass or blurred surface", r"backdrop-(?:filter|blur)|backdrop-filter\s*:\s*blur|bg-white/(?:5|10|15|20)\b"),
    rule("A13", "review", "hover lift or scale; verify the element is interactive", r"hover:(?:-?translate-y|scale-|shadow-(?:xl|2xl))"),
    rule("B3", "cluster", "icon tile styling", r"rounded-(?:lg|xl|2xl)[^\n]{0,120}bg-[a-z]+-(?:50|100)[^\n]{0,80}p-[23]\b|bg-(?:primary|accent)/(?:5|10|15)[^\n]{0,100}rounded"),
    rule("B5", "cluster", "large pill or blob radius", r"rounded-(?:full|2xl|3xl)|border-radius\s*:\s*(?:9999|999|100|50)px"),
    rule("B6", "cluster", "decorative gradient or glow", r"bg-gradient-to-|linear-gradient\(|radial-gradient\(|conic-gradient\(|\bblur-3xl\b"),
    rule("B7", "cluster", "generic reveal, marquee, or transition-all", r"fade-?up|fadeInUp|data-aos|whileInView|animate-(?:fade|marquee)|transition\s*:\s*all|\btransition-all\b"),
    rule("B11", "cluster", "generic transformation copy", r"\b(?:unlock your|elevate your|supercharge|all-in-one|everything you need|trusted by|join thousands|solu[cç][aã]o completa|tudo em um s[oó] lugar|sem complica[cç][aã]o|potencialize|revolucione)\b"),
    rule("E2", "strong", "scroll cue or bounce prompt", r"scroll (?:down|to explore)|role (?:pra|para) (?:baixo|explorar)|animate-bounce"),
    rule("E4", "review", "version or launch-status pill text", r">\s*(?:beta|early access|invite-only|v0?\.\d|coming soon)\s*<"),
    rule("E6", "cluster", "decorative grid background", r"repeating-linear-gradient|bg-grid|background-size\s*:\s*\d+px\s+\d+px|\[background-size:[^\]]+\]"),
    rule("E9", "cluster", "spring or overshoot easing", r"easeOutBack|easeInBack|elastic|backOut|cubic-bezier\([^)]*,\s*-[0-9.]"),
    rule("E13", "weak", "neutral gray text on saturated surface", r"bg-(?:indigo|violet|purple|blue|emerald|rose|teal|sky|cyan)-(?:500|600|700|800)[^\n]{0,120}text-(?:gray|zinc|slate|neutral|stone)-(?:300|400|500)"),
    rule("E14", "weak", "justified body text; verify content role", r"text-align\s*:\s*justify|\btext-justify\b"),
    rule("Q1", "quality", "focus outline removed; verify an equally visible replacement", r"\boutline-none\b|outline\s*:\s*none"),
)


def iter_files(inputs: list[str]):
    seen: set[Path] = set()
    for raw in inputs:
        target = Path(raw)
        candidates = [target] if target.is_file() else target.rglob("*") if target.is_dir() else []
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.lower() not in SOURCE_EXTENSIONS:
                continue
            if SKIP_DIRECTORIES.intersection(candidate.parts):
                continue
            resolved = candidate.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield candidate


def scan_line(path: Path, number: int, text: str) -> list[dict[str, object]]:
    ignored = set()
    if IGNORE_MARKER in text:
        ignored = set(re.findall(r"(?:A|B|C|E|Q)\d{1,2}", text.split(IGNORE_MARKER, 1)[1]))
    findings = []
    for current in RULES:
        if current.code in ignored:
            continue
        match = current.pattern.search(text)
        if not match:
            continue
        if current.code == "Q1" and "focus-visible" in text:
            continue
        start = max(0, match.start() - 45)
        end = min(len(text), match.end() + 65)
        findings.append({
            "file": str(path),
            "line": number,
            "code": current.code,
            "level": current.level,
            "description": current.description,
            "excerpt": text[start:end].strip(),
        })
    return findings


def scan(inputs: list[str]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in iter_files(inputs):
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for number, text in enumerate(lines, 1):
            findings.extend(scan_line(path, number, text[:4000]))
    return findings


def self_test() -> int:
    samples = {
        "A1": '<span class="uppercase tracking-widest">Features</span>',
        "A2": '<span class="bg-clip-text text-transparent">Future</span>',
        "A7": '<span class="animate-pulse">Live</span>',
        "A12": '<div class="backdrop-blur-xl bg-white/10">',
        "A13": '<div class="hover:-translate-y-1">',
        "B7": '<div class="transition-all">',
        "B11": '<h1>Unlock your potential with our all-in-one platform</h1>',
        "Q1": '<button class="outline-none">Save</button>',
    }
    for expected, sample in samples.items():
        codes = {item["code"] for item in scan_line(Path("self-test.tsx"), 1, sample)}
        if expected not in codes:
            print(f"self-test failed: {expected}", file=sys.stderr)
            return 1
    print("self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true", help="exit 2 when three or more distinct rule categories appear")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.paths:
        parser.error("provide at least one file or directory")

    findings = scan(args.paths)
    distinct = sorted({item["code"] for item in findings})

    if args.as_json:
        print(json.dumps({"findings": findings, "distinct_rules": distinct}, indent=2, ensure_ascii=False))
    else:
        for item in findings:
            print(f'{item["file"]}:{item["line"]} [{item["level"]}/{item["code"]}] {item["description"]} | {item["excerpt"]}')
        print(f"\n{len(findings)} finding(s) across {len(distinct)} rule category/categories.")
        print("Review context and the rendered UI; individual matches may be intentional.")

    return 2 if args.strict and len(distinct) >= 3 else 0


if __name__ == "__main__":
    raise SystemExit(main())
