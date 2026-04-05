#!/usr/bin/env python3
"""
Landing Page Wireframe Generator
Generates ASCII/text-based wireframe visualizations for landing pages

Usage:
    python wireframe_generator.py --sections hero,value,trust,benefits,faq,cta,final
    python wireframe_generator.py --type saas_free_trial
    python wireframe_generator.py --full
"""

import argparse
import json
from typing import List, Dict

# Section wireframe components
WIREFRAMES = {
    "hero": """
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⭐ TRUST MICRO-BAR: [stat/social proof]                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ╔═══════════════════════════════════════════════════════════════════╗    │
│   ║                                                                   ║    │
│   ║   HEADLINE: [Dream outcome statement]                             ║    │
│   ║   ─────────────────────────────────────────────────────────────   ║    │
│   ║   Subhead: [How + Timeframe + Proof element]                     ║    │
│   ║                                                                   ║    │
│   ║   ┌─────────────────────────┐                                    ║    │
│   ║   │  ★ PRIMARY CTA ★        │                                    ║    │
│   ║   └─────────────────────────┘                                    ║    │
│   ║   ✓ No credit card  ✓ Setup in 2 min  ✓ Cancel anytime          ║    │
│   ║                                                                   ║    │
│   ╚═══════════════════════════════════════════════════════════════════╝    │
│                                    │                                        │
│   ┌──────────────────────────────────────────────────────────────────┐     │
│   │                                                                  │     │
│   │                    HERO IMAGE / VIDEO                            │     │
│   │                  [Product screenshot or                          │     │
│   │                   transformation visual]                         │     │
│   │                                                                  │     │
│   └──────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│   LOGO BAR: [Logo] [Logo] [Logo] [Logo] [Logo]                             │
│   "Trusted by leading companies"                                           │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "value": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   SECTION HEADLINE: "Here's How It Works"                                  │
│   ═══════════════════════════════════════════════════════════════════════  │
│                                                                             │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐           │
│   │       (1)       │  │       (2)       │  │       (3)       │           │
│   │   ┌───────┐     │  │   ┌───────┐     │  │   ┌───────┐     │           │
│   │   │ ICON  │     │  │   │ ICON  │     │  │   │ ICON  │     │           │
│   │   └───────┘     │  │   └───────┘     │  │   └───────┘     │           │
│   │                 │  │                 │  │                 │           │
│   │   Step Title    │  │   Step Title    │  │   Step Title    │           │
│   │   ───────────   │  │   ───────────   │  │   ───────────   │           │
│   │   Brief desc    │  │   Brief desc    │  │   Brief desc    │           │
│   │   of action     │  │   of action     │  │   of action     │           │
│   │                 │  │                 │  │                 │           │
│   │   → Outcome     │  │   → Outcome     │  │   → Outcome     │           │
│   │                 │  │                 │  │                 │           │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘           │
│                                                                             │
│   ┌─────────────────────────┐                                              │
│   │     SECONDARY CTA       │  ← Repeat for those ready after value prop  │
│   └─────────────────────────┘                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "trust": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   SECTION HEADLINE: "What Our Customers Say"                               │
│   ═══════════════════════════════════════════════════════════════════════  │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │  ┌─────┐                                                          │    │
│   │  │PHOTO│  "Testimonial quote with specific outcome and metrics.   │    │
│   │  └─────┘   This should be 2-3 sentences showing transformation."  │    │
│   │                                                                    │    │
│   │            — Full Name, Title at Company                          │    │
│   │            ⭐⭐⭐⭐⭐                                               │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │  ┌─────┐                                                          │    │
│   │  │PHOTO│  "Second testimonial focusing on ease/speed of results." │    │
│   │  └─────┘                                                          │    │
│   │            — Full Name, Title at Company                          │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │  ┌─────┐                                                          │    │
│   │  │PHOTO│  "Third testimonial addressing skepticism overcome."     │    │
│   │  └─────┘                                                          │    │
│   │            — Full Name, Title at Company                          │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  STATS BAR: [X]+ Customers  |  [Y]% Satisfaction  |  [Z] Rating │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "benefits": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   SECTION HEADLINE: "Everything You Need to [Achieve Outcome]"             │
│   ═══════════════════════════════════════════════════════════════════════  │
│                                                                             │
│   ┌─────────────────────────┐     ┌─────────────────────────┐              │
│   │  🎯 BENEFIT 1           │     │  📊 BENEFIT 2           │              │
│   │  ─────────────────────  │     │  ─────────────────────  │              │
│   │  Outcome-focused desc   │     │  Outcome-focused desc   │              │
│   │  (not feature)          │     │  (not feature)          │              │
│   └─────────────────────────┘     └─────────────────────────┘              │
│                                                                             │
│   ┌─────────────────────────┐     ┌─────────────────────────┐              │
│   │  🚀 BENEFIT 3           │     │  ⚡ BENEFIT 4           │              │
│   │  ─────────────────────  │     │  ─────────────────────  │              │
│   │  Outcome-focused desc   │     │  Outcome-focused desc   │              │
│   │  (not feature)          │     │  (not feature)          │              │
│   └─────────────────────────┘     └─────────────────────────┘              │
│                                                                             │
│   ┌─────────────────────────┐     ┌─────────────────────────┐              │
│   │  🔒 BENEFIT 5           │     │  💬 BENEFIT 6           │              │
│   │  ─────────────────────  │     │  ─────────────────────  │              │
│   │  Outcome-focused desc   │     │  Outcome-focused desc   │              │
│   │  (not feature)          │     │  (not feature)          │              │
│   └─────────────────────────┘     └─────────────────────────┘              │
│                                                                             │
│   ┌─────────────────────────┐                                              │
│   │     PRIMARY CTA         │  ← Repeat CTA after benefits                 │
│   └─────────────────────────┘                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "faq": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   SECTION HEADLINE: "Frequently Asked Questions"                           │
│   ═══════════════════════════════════════════════════════════════════════  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ▼ Q: Will this work for my specific situation?                  │      │
│   │     A: [Validate → Answer → Proof → Bridge to action]           │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ▼ Q: What's the investment/pricing?                            │      │
│   │     A: [ROI framing + value comparison]                         │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ▼ Q: How much time does it take?                               │      │
│   │     A: [Simplicity emphasis + support available]                │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ▼ Q: Do I need technical skills?                               │      │
│   │     A: [No technical skills required framing]                   │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ▼ Q: What if it doesn't work for me?                           │      │
│   │     A: [Guarantee details + proof]                              │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   Still have questions? [Contact link] — we're here to help.               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "cta": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   CTA STRATEGY VISUALIZATION                                               │
│   ═══════════════════════════════════════════════════════════════════════  │
│                                                                             │
│   PLACEMENT MAP:                                                           │
│                                                                             │
│   ┌─────────────────────────────┐                                          │
│   │ HERO: ★ PRIMARY CTA (1)     │ ← First touchpoint, above fold          │
│   │       + micro-copy          │                                          │
│   └─────────────────────────────┘                                          │
│                ↓                                                            │
│   ┌─────────────────────────────┐                                          │
│   │ VALUE: ★ PRIMARY CTA (2)    │ ← After explaining value                │
│   │       + secondary option    │                                          │
│   └─────────────────────────────┘                                          │
│                ↓                                                            │
│   ┌─────────────────────────────┐                                          │
│   │ BENEFITS: ★ PRIMARY CTA (3) │ ← After listing benefits                │
│   └─────────────────────────────┘                                          │
│                ↓                                                            │
│   ┌─────────────────────────────┐                                          │
│   │ TRUST: ★ PRIMARY CTA (4)    │ ← Peak believability moment             │
│   │       + micro-testimonial   │                                          │
│   └─────────────────────────────┘                                          │
│                ↓                                                            │
│   ┌─────────────────────────────┐                                          │
│   │ FINAL: ★★ BIG CTA (5) ★★    │ ← Last chance + urgency                 │
│   │       + guarantee           │                                          │
│   └─────────────────────────────┘                                          │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │ STICKY BAR: [Offer reminder] [CTA BUTTON]  ← Appears after scroll │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
""",
    
    "final": """
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  ⏰ URGENCY ELEMENT: [Countdown / Scarcity / Deadline]           │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│   ╔═══════════════════════════════════════════════════════════════════╗    │
│   ║                                                                   ║    │
│   ║   "Ready to [Dream Outcome]?"                                     ║    │
│   ║                                                                   ║    │
│   ║   [One-sentence value recap covering key benefits]                ║    │
│   ║                                                                   ║    │
│   ║   ✓ [Key benefit 1]                                              ║    │
│   ║   ✓ [Key benefit 2]                                              ║    │
│   ║   ✓ [Key benefit 3]                                              ║    │
│   ║   ✓ [Guarantee/bonus]                                            ║    │
│   ║                                                                   ║    │
│   ║   ┌─────────────────────────────────────────────────────────┐    ║    │
│   ║   │                                                         │    ║    │
│   ║   │            ★★★ PRIMARY CTA (LARGEST) ★★★                │    ║    │
│   ║   │                                                         │    ║    │
│   ║   └─────────────────────────────────────────────────────────┘    ║    │
│   ║                                                                   ║    │
│   ║   ✓ [Final friction reducer]  ✓ [Guarantee reminder]            ║    │
│   ║                                                                   ║    │
│   ╚═══════════════════════════════════════════════════════════════════╝    │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │  > "[Best testimonial — short, powerful, outcome-focused]"       │      │
│   │    — Name, Title                                                │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
"""
}


def generate_full_page_wireframe() -> str:
    """Generate complete landing page wireframe"""
    sections = ["hero", "value", "trust", "benefits", "faq", "final"]
    
    output = []
    output.append("=" * 79)
    output.append("LANDING PAGE WIREFRAME — FULL STRUCTURE")
    output.append("Generated by Manu LP v1.0")
    output.append("=" * 79)
    output.append("")
    
    for i, section in enumerate(sections, 1):
        output.append(f"SECTION {i}: {section.upper()}")
        output.append("-" * 79)
        output.append(WIREFRAMES.get(section, "[Section not found]"))
        output.append("")
    
    output.append("=" * 79)
    output.append("END WIREFRAME")
    output.append("=" * 79)
    
    return "\n".join(output)


def generate_section_wireframe(sections: List[str]) -> str:
    """Generate wireframe for specific sections"""
    output = []
    output.append("=" * 79)
    output.append(f"LANDING PAGE WIREFRAME — SELECTED SECTIONS: {', '.join(sections).upper()}")
    output.append("=" * 79)
    output.append("")
    
    for section in sections:
        section_lower = section.lower().strip()
        if section_lower in WIREFRAMES:
            output.append(f"SECTION: {section_lower.upper()}")
            output.append("-" * 79)
            output.append(WIREFRAMES[section_lower])
            output.append("")
        else:
            output.append(f"[Section '{section}' not found. Available: {', '.join(WIREFRAMES.keys())}]")
            output.append("")
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Generate landing page wireframes")
    parser.add_argument("--sections", type=str, help="Comma-separated list of sections")
    parser.add_argument("--full", action="store_true", help="Generate full page wireframe")
    parser.add_argument("--list", action="store_true", help="List available sections")
    
    args = parser.parse_args()
    
    if args.list:
        print("Available sections:", ", ".join(WIREFRAMES.keys()))
        return
    
    if args.full:
        print(generate_full_page_wireframe())
    elif args.sections:
        sections = [s.strip() for s in args.sections.split(",")]
        print(generate_section_wireframe(sections))
    else:
        print(generate_full_page_wireframe())


if __name__ == "__main__":
    main()
