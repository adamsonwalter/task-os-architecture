#!/usr/bin/env python3
"""
render_sop.py — Convert sop_source.md into a professional, client-ready sop.html

Usage:
    python scripts/render_sop.py                  # renders docs/sop_source.md → docs/sop.html
    python scripts/render_sop.py path/to/src.md   # renders custom source → docs/sop.html
    python scripts/render_sop.py src.md out.html   # renders custom source → custom output

Requires: pip install markdown (Python-Markdown)
If not installed, falls back to a built-in lightweight converter.
"""

import sys
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Resolve paths
# ---------------------------------------------------------------------------
base = Path(__file__).resolve().parents[1]

if len(sys.argv) >= 3:
    src_path = Path(sys.argv[1]).resolve()
    out_path = Path(sys.argv[2]).resolve()
elif len(sys.argv) == 2:
    src_path = Path(sys.argv[1]).resolve()
    out_path = base / "docs" / "sop.html"
else:
    src_path = base / "docs" / "sop_source.md"
    out_path = base / "docs" / "sop.html"

if not src_path.exists():
    print(f"ERROR: Source file not found: {src_path}")
    sys.exit(1)

source = src_path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# Markdown → HTML conversion
# ---------------------------------------------------------------------------
try:
    import markdown
    body_html = markdown.markdown(
        source,
        extensions=["tables", "fenced_code", "smarty", "toc"],
        extension_configs={"toc": {"toc_depth": "2-3"}},
    )
except ImportError:
    # Lightweight fallback — handles headings, lists, bold, code blocks, tables, hr
    def _fallback_md(md_text):
        lines = md_text.split("\n")
        html_lines = []
        in_list = False
        in_code = False
        in_table = False
        table_header_done = False

        for line in lines:
            stripped = line.strip()

            # Fenced code blocks
            if stripped.startswith("```"):
                if in_code:
                    html_lines.append("</code></pre>")
                    in_code = False
                else:
                    html_lines.append("<pre><code>")
                    in_code = True
                continue
            if in_code:
                import html as _h
                html_lines.append(_h.escape(line))
                continue

            # Horizontal rule
            if re.match(r"^-{3,}$|^\*{3,}$|^_{3,}$", stripped):
                if in_list:
                    html_lines.append("</ol>" if html_lines[-1].startswith("<li>") else "</ul>")
                    in_list = False
                html_lines.append("<hr>")
                continue

            # Headings
            m = re.match(r"^(#{1,6})\s+(.*)", stripped)
            if m:
                if in_list:
                    html_lines.append("</ol>")
                    in_list = False
                if in_table:
                    html_lines.append("</tbody></table>")
                    in_table = False
                level = len(m.group(1))
                text = _inline(m.group(2))
                html_lines.append(f"<h{level}>{text}</h{level}>")
                continue

            # Tables
            if "|" in stripped and stripped.startswith("|"):
                cells = [c.strip() for c in stripped.split("|")[1:-1]]
                if all(re.match(r"^[-:]+$", c) for c in cells):
                    continue  # separator row
                if not in_table:
                    html_lines.append('<table><thead><tr>')
                    html_lines.append("".join(f"<th>{_inline(c)}</th>" for c in cells))
                    html_lines.append("</tr></thead><tbody>")
                    in_table = True
                    table_header_done = True
                else:
                    html_lines.append("<tr>")
                    html_lines.append("".join(f"<td>{_inline(c)}</td>" for c in cells))
                    html_lines.append("</tr>")
                continue
            elif in_table:
                html_lines.append("</tbody></table>")
                in_table = False

            # Ordered list
            m = re.match(r"^(\d+)\.\s+(.*)", stripped)
            if m:
                if not in_list:
                    html_lines.append("<ol>")
                    in_list = True
                html_lines.append(f"<li>{_inline(m.group(2))}</li>")
                continue

            # Unordered list
            m = re.match(r"^[-*]\s+(.*)", stripped)
            if m:
                if not in_list:
                    html_lines.append("<ul>")
                    in_list = True
                html_lines.append(f"<li>{_inline(m.group(1))}</li>")
                continue

            if in_list and stripped == "":
                html_lines.append("</ol>" if any("<ol>" in l for l in html_lines[-10:]) else "</ul>")
                in_list = False

            # Paragraphs
            if stripped == "":
                html_lines.append("")
                continue
            html_lines.append(f"<p>{_inline(stripped)}</p>")

        if in_list:
            html_lines.append("</ol>" if any("<ol>" in l for l in html_lines[-10:]) else "</ul>")
        if in_table:
            html_lines.append("</tbody></table>")
        return "\n".join(html_lines)

    def _inline(text):
        """Handle bold, italic, inline code, links."""
        import html as _h
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
        return text

    body_html = _fallback_md(source)

# ---------------------------------------------------------------------------
# Extract title from first H1 or filename
# ---------------------------------------------------------------------------
title_match = re.search(r"^#\s+(.+)", source, re.MULTILINE)
doc_title = title_match.group(1).strip() if title_match else src_path.stem.replace("_", " ").title()

# ---------------------------------------------------------------------------
# HTML template — premium consulting style, print-ready, mobile-responsive
# ---------------------------------------------------------------------------
html_output = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{doc_title}</title>
  <style>
    /* ── Token Architecture (Executive Light pillar) ── */
    :root {{
      --bg-page:      #f5f4f0;
      --bg-surface:   #ffffff;
      --bg-raised:    #f0ede6;
      --text-heading: #0a0a0a;
      --text-body:    #1a1a1a;
      --text-meta:    #8a8680;
      --border:       #d8d4cc;
      --accent:       #2563eb;
      --accent-fg:    #ffffff;
      --font-sans:    -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", sans-serif;
    }}

    /* ── Reset & Base ── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: var(--font-sans);
      background: var(--bg-page);
      color: var(--text-body);
      line-height: 1.7;
      font-size: 15px;
      -webkit-font-smoothing: antialiased;
    }}

    /* ── Layout (8pt grid) ── */
    .page {{
      max-width: 820px;
      margin: 64px auto;
      padding: 0 24px;
    }}

    .document {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 48px 48px 40px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    /* ── Typography ── */
    h1 {{
      font-size: 1.75rem;
      font-weight: 700;
      color: var(--text-heading);
      margin-bottom: 8px;
      letter-spacing: -0.02em;
      line-height: 1.25;
    }}

    h2 {{
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--text-heading);
      margin-top: 32px;
      margin-bottom: 12px;
      padding-bottom: 6px;
      border-bottom: 2px solid var(--accent);
      letter-spacing: -0.01em;
    }}

    h3 {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-heading);
      margin-top: 24px;
      margin-bottom: 8px;
    }}

    p {{
      margin-bottom: 12px;
      max-width: 65ch;
    }}

    /* ── Lists ── */
    ol, ul {{
      margin: 8px 0 16px 0;
      padding-left: 24px;
    }}

    li {{
      margin-bottom: 8px;
      max-width: 65ch;
    }}

    li::marker {{
      color: var(--accent);
      font-weight: 600;
    }}

    /* ── Steps (ordered list special treatment) ── */
    ol {{
      counter-reset: step;
      list-style: none;
      padding-left: 0;
    }}

    ol > li {{
      counter-increment: step;
      position: relative;
      padding-left: 40px;
      margin-bottom: 16px;
    }}

    ol > li::before {{
      content: counter(step);
      position: absolute;
      left: 0;
      top: 1px;
      width: 26px;
      height: 26px;
      background: var(--accent);
      color: var(--accent-fg);
      border-radius: 50%;
      font-size: 0.8rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
    }}

    /* ── Tables ── */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0 24px;
      font-size: 0.9rem;
    }}

    th {{
      background: var(--bg-raised);
      color: var(--text-heading);
      font-weight: 600;
      text-align: left;
      padding: 10px 14px;
      border-bottom: 2px solid var(--border);
    }}

    td {{
      padding: 9px 14px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }}

    tr:last-child td {{
      border-bottom: none;
    }}

    /* ── Code ── */
    code {{
      font-family: "SF Mono", "Fira Code", "Consolas", monospace;
      font-size: 0.85em;
      background: var(--bg-raised);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--text-heading);
    }}

    pre {{
      background: var(--bg-raised);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 16px 20px;
      overflow-x: auto;
      margin: 16px 0;
      line-height: 1.5;
    }}

    pre code {{
      background: none;
      padding: 0;
      font-size: 0.85rem;
    }}

    /* ── Inline ── */
    strong {{ color: var(--text-heading); }}

    a {{
      color: var(--accent);
      text-decoration: none;
      border-bottom: 1px solid transparent;
      transition: border-color 0.15s;
    }}

    a:hover {{
      border-bottom-color: var(--accent);
    }}

    hr {{
      border: none;
      border-top: 1px solid var(--border);
      margin: 32px 0;
    }}

    /* ── Meta header ── */
    .meta {{
      color: var(--text-meta);
      font-size: 0.8rem;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }}

    .meta span + span::before {{
      content: " · ";
    }}

    /* ── Gate / callout styling ── */
    p:has(strong:first-child) {{
      background: var(--bg-raised);
      border-left: 3px solid var(--accent);
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 12px 0;
    }}

    /* ── Print ── */
    @media print {{
      body {{ background: #fff; font-size: 12pt; }}
      .page {{ margin: 0; padding: 0; }}
      .document {{ border: none; box-shadow: none; padding: 0; }}
      h2 {{ page-break-after: avoid; }}
      ol > li::before {{ background: #333; color: #fff; }}
    }}

    /* ── Mobile ── */
    @media (max-width: 640px) {{
      .document {{ padding: 24px 20px; }}
      h1 {{ font-size: 1.4rem; }}
      .page {{ margin: 24px auto; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="document">
      <div class="meta">
        <span>Standard Operating Procedure</span>
        <span>Generated from <code>{src_path.name}</code></span>
      </div>
      {body_html}
    </div>
  </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Write output
# ---------------------------------------------------------------------------
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(html_output, encoding="utf-8")
print(f"✓ Rendered: {out_path}")
print(f"  Source:   {src_path}")
print(f"  Size:     {out_path.stat().st_size:,} bytes")
