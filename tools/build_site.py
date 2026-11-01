#!/usr/bin/env python3
"""
turkish-prepper Static Site Builder
Markdown dokümanlarını Kiwix / ZIM uyumlu modern, çevrimdışı ve duyarlı (responsive) bir statik siteye dönüştürür.
Sıfır bağımlılık: Harici kütüphane gerektirmez (Standart Python 3 ile çalışır).
"""

import os
import re
import html
import struct
import zlib
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
GLOSSARY_DIR = BASE_DIR / "glossary"
OUTPUT_DIR = BASE_DIR / "site"

def generate_icon(dest_path: Path):
    """Generates a standalone 48x48 RGBA PNG icon in pure Python."""
    width, height = 48, 48
    color = (230, 57, 70, 255) # Red #e63946
    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0) # filter type
        for x in range(width):
            raw_data.extend(color)
    compressed = zlib.compress(bytes(raw_data))
    
    png = bytearray(b'\x89PNG\r\n\x1a\n')
    def chunk(tag, data):
        c = bytearray(struct.pack('>I', len(data)))
        c.extend(tag)
        c.extend(data)
        crc = zlib.crc32(tag + data) & 0xffffffff
        c.extend(struct.pack('>I', crc))
        return c
        
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    png.extend(chunk(b'IHDR', ihdr))
    png.extend(chunk(b'IDAT', compressed))
    png.extend(chunk(b'IEND', b''))
    dest_path.write_bytes(bytes(png))

CSS_STYLES = """
:root {
  --bg-color: #0d1117;
  --surface-color: #161b22;
  --border-color: #30363d;
  --text-main: #c9d1d9;
  --text-muted: #8b949e;
  --primary: #e63946;
  --primary-light: #ff6b6b;
  --accent: #457b9d;
  --code-bg: #1f242c;
  --alert-bg: #1c2128;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-color);
  color: var(--text-main);
  line-height: 1.6;
}

.layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 320px;
  background-color: var(--surface-color);
  border-right: 1px solid var(--border-color);
  padding: 24px 16px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  text-decoration: none;
  color: #fff;
}
.brand h2 { font-size: 1.25rem; font-weight: 700; color: var(--primary-light); }
.brand span { font-size: 0.8rem; color: var(--text-muted); display: block; }

.search-box {
  width: 100%;
  padding: 10px 14px;
  background: var(--code-bg);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-main);
  margin-bottom: 20px;
  font-size: 0.9rem;
}
.search-box:focus { outline: none; border-color: var(--primary-light); }

.nav-group { margin-bottom: 20px; }
.nav-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 8px;
  font-weight: 600;
}
.nav-list { list-style: none; }
.nav-item { margin-bottom: 4px; }
.nav-link {
  display: block;
  padding: 8px 12px;
  color: var(--text-main);
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: background 0.15s, color 0.15s;
}
.nav-link:hover, .nav-link.active {
  background: var(--border-color);
  color: #fff;
}

.content {
  flex: 1;
  max-width: 900px;
  padding: 40px 48px;
  margin: 0 auto;
}

h1 { font-size: 2rem; margin-bottom: 16px; color: #fff; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
h2 { font-size: 1.5rem; margin-top: 32px; margin-bottom: 12px; color: #f0f6fc; }
h3 { font-size: 1.2rem; margin-top: 24px; margin-bottom: 8px; color: #f0f6fc; }
p { margin-bottom: 16px; }

blockquote {
  border-left: 4px solid var(--primary);
  background: var(--alert-bg);
  padding: 14px 18px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 20px;
  color: #e6edf3;
}

ul, ol { margin-left: 24px; margin-bottom: 16px; }
li { margin-bottom: 6px; }

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 24px;
}
th, td {
  padding: 10px 14px;
  border: 1px solid var(--border-color);
  text-align: left;
}
th { background: var(--surface-color); color: #fff; }
tr:nth-child(even) { background: rgba(255,255,255,0.02); }

code {
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.9em;
}

pre {
  background: var(--code-bg);
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  margin-bottom: 20px;
  border: 1px solid var(--border-color);
}

.badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-right: 6px;
}
.badge-danger { background: #b91c1c; color: #fff; }
.badge-warning { background: #b45309; color: #fff; }
.badge-success { background: #15803d; color: #fff; }

@media (max-width: 800px) {
  .layout { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: relative; }
  .content { padding: 20px; }
}
"""

JS_SCRIPT = """
function filterNav() {
  const query = document.getElementById('search').value.toLowerCase();
  const items = document.querySelectorAll('.nav-item');
  items.forEach(item => {
    const text = item.textContent.toLowerCase();
    item.style.display = text.includes(query) ? '' : 'none';
  });
}
"""

def parse_simple_markdown(text: str) -> str:
    """Minimal, self-contained Markdown to HTML converter."""
    lines = text.split("\n")
    html_out = []
    in_table = False
    in_list = False
    list_tag = "ul"
    in_quote = False
    in_code = False
    
    for line in lines:
        stripped = line.strip()
        
        # Code blocks
        if stripped.startswith("```"):
            if in_code:
                html_out.append("</code></pre>")
                in_code = False
            else:
                html_out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            html_out.append(html.escape(line))
            continue
            
        # Blockquotes
        if stripped.startswith(">"):
            content = stripped.lstrip("> ").strip()
            if not in_quote:
                html_out.append("<blockquote>")
                in_quote = True
            html_out.append(f"<p>{inline_format(content)}</p>")
            continue
        elif in_quote:
            html_out.append("</blockquote>")
            in_quote = False
            
        # Tables
        if "|" in line and (line.startswith("|") or line.endswith("|")):
            if "---" in line:
                continue # delimiter
            cols = [c.strip() for c in line.split("|") if c.strip() or line.startswith("|")]
            if cols and cols[0] == "": cols = cols[1:]
            if cols and cols[-1] == "": cols = cols[:-1]
            
            if not in_table:
                html_out.append("<table><thead><tr>")
                for c in cols:
                    html_out.append(f"<th>{inline_format(c)}</th>")
                html_out.append("</tr></thead><tbody>")
                in_table = True
            else:
                html_out.append("<tr>")
                for c in cols:
                    html_out.append(f"<td>{inline_format(c)}</td>")
                html_out.append("</tr>")
            continue
        elif in_table:
            html_out.append("</tbody></table>")
            in_table = False
            
        # Headers
        if stripped.startswith("### "):
            html_out.append(f"<h3>{inline_format(stripped[4:])}</h3>")
            continue
        if stripped.startswith("## "):
            html_out.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            continue
        if stripped.startswith("# "):
            html_out.append(f"<h1>{inline_format(stripped[2:])}</h1>")
            continue
            
        # Lists
        if stripped.startswith("* ") or stripped.startswith("- "):
            if not in_list:
                html_out.append("<ul>")
                in_list = True
                list_tag = "ul"
            html_out.append(f"<li>{inline_format(stripped[2:])}</li>")
            continue
        elif re.match(r"^\d+\.\s", stripped):
            match = re.match(r"^\d+\.\s", stripped)
            if not in_list:
                html_out.append("<ol>")
                in_list = True
                list_tag = "ol"
            html_out.append(f"<li>{inline_format(stripped[len(match.group(0)):])}</li>")
            continue
        elif in_list:
            html_out.append(f"</{list_tag}>")
            in_list = False
            
        if stripped == "---":
            html_out.append("<hr style='border:0; border-top:1px solid var(--border-color); margin:24px 0;'/>")
            continue
            
        if stripped:
            html_out.append(f"<p>{inline_format(stripped)}</p>")
            
    if in_table: html_out.append("</tbody></table>")
    if in_list: html_out.append(f"</{list_tag}>")
    if in_quote: html_out.append("</blockquote>")
    if in_code: html_out.append("</code></pre>")
    
    return "\n".join(html_out)

def inline_format(text: str) -> str:
    # Bold + Italic
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # Bold
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)
    # Markdown links
    text = re.sub(r"\[(.*?)\]\((.*?)\.md\)", r'<a href="\2.html" style="color:var(--primary-light);">\1</a>', text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" style="color:var(--primary-light);">\1</a>', text)
    return text

def build():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate favicon / illustration for Kiwix ZIM
    generate_icon(OUTPUT_DIR / "icon.png")
    
    # Collect all docs
    pages = []
    
    # Add root README as index
    readme_path = BASE_DIR / "README.md"
    if readme_path.exists():
        pages.append({
            "title": "Giriş ve Genel Bakış",
            "category": "Genel",
            "path": readme_path,
            "out_name": "index.html"
        })
        
    if DOCS_DIR.exists():
        for cat_dir in sorted(DOCS_DIR.iterdir()):
            if cat_dir.is_dir():
                cat_name = cat_dir.name.replace("-", " ").title()
                for md_file in sorted(cat_dir.glob("*.md")):
                    title = md_file.stem.replace("-", " ").title()
                    pages.append({
                        "title": title,
                        "category": cat_name,
                        "path": md_file,
                        "out_name": f"{cat_dir.name}_{md_file.stem}.html"
                    })
                
    if GLOSSARY_DIR.exists():
        for md_file in sorted(GLOSSARY_DIR.glob("*.md")):
            pages.append({
                "title": "Tıbbi & Teknik Terimler",
                "category": "Sözlük",
                "path": md_file,
                "out_name": f"glossary_{md_file.stem}.html"
            })

    # Render each page
    for page in pages:
        content_text = page["path"].read_text(encoding="utf-8")
        parsed_html = parse_simple_markdown(content_text)
        
        # Build Navigation
        nav_html = []
        categories = {}
        for p in pages:
            categories.setdefault(p["category"], []).append(p)
            
        for cat, cat_pages in categories.items():
            nav_html.append(f'<div class="nav-group"><div class="nav-title">{cat}</div><ul class="nav-list">')
            for cp in cat_pages:
                active_cls = ' active' if cp["out_name"] == page["out_name"] else ''
                nav_html.append(f'<li class="nav-item"><a class="nav-link{active_cls}" href="{cp["out_name"]}">{cp["title"]}</a></li>')
            nav_html.append('</ul></div>')
            
        full_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="icon.png">
  <title>{page["title"]} - Turkish Prepper</title>
  <style>{CSS_STYLES}</style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <a href="index.html" class="brand">
        <div>
          <h2>turkish-prepper 🇹🇷</h2>
          <span>Çevrimdışı Afet Bilgi Havuzu</span>
        </div>
      </a>
      <input type="text" id="search" class="search-box" placeholder="Rehberlerde ara..." onkeyup="filterNav()">
      <nav>
        {''.join(nav_html)}
      </nav>
    </aside>
    <main class="content">
      {parsed_html}
    </main>
  </div>
  <script>{JS_SCRIPT}</script>
</body>
</html>"""
        (OUTPUT_DIR / page["out_name"]).write_text(full_html, encoding="utf-8")
        
    print(f"Toplam {len(pages)} sayfa 'site/' dizinine basariyla derlendi!")

if __name__ == "__main__":
    build()
