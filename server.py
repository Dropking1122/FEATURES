import http.server
import socketserver
import os
import markdown
import urllib.parse
from pathlib import Path

PORT = 5000
HOST = "0.0.0.0"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d1117; color: #c9d1d9; line-height: 1.6; }}
  .sidebar {{ position: fixed; left: 0; top: 0; width: 260px; height: 100vh; background: #161b22; border-right: 1px solid #30363d; overflow-y: auto; padding: 20px 0; z-index: 100; }}
  .sidebar h2 {{ color: #58a6ff; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; padding: 0 20px 12px; border-bottom: 1px solid #30363d; margin-bottom: 12px; }}
  .sidebar a {{ display: block; padding: 8px 20px; color: #8b949e; text-decoration: none; font-size: 13px; transition: all 0.15s; }}
  .sidebar a:hover, .sidebar a.active {{ color: #58a6ff; background: #1c2128; border-left: 3px solid #58a6ff; padding-left: 17px; }}
  .sidebar .section {{ margin-bottom: 8px; }}
  .sidebar .section-title {{ color: #e6edf3; font-weight: 600; font-size: 12px; padding: 6px 20px 4px; text-transform: uppercase; letter-spacing: 0.5px; }}
  .main {{ margin-left: 260px; min-height: 100vh; }}
  .content {{ max-width: 900px; margin: 0 auto; padding: 40px 40px; }}
  h1 {{ color: #e6edf3; font-size: 2em; border-bottom: 1px solid #30363d; padding-bottom: 12px; margin: 24px 0 16px; }}
  h2 {{ color: #e6edf3; font-size: 1.5em; border-bottom: 1px solid #21262d; padding-bottom: 8px; margin: 24px 0 12px; }}
  h3 {{ color: #e6edf3; font-size: 1.2em; margin: 20px 0 8px; }}
  h4 {{ color: #c9d1d9; margin: 16px 0 8px; }}
  p {{ margin: 12px 0; }}
  a {{ color: #58a6ff; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  code {{ background: #161b22; border: 1px solid #30363d; border-radius: 4px; padding: 2px 6px; font-family: 'SF Mono', Consolas, monospace; font-size: 85%; color: #ff7b72; }}
  pre {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; overflow-x: auto; margin: 16px 0; }}
  pre code {{ background: none; border: none; padding: 0; color: #e6edf3; }}
  blockquote {{ border-left: 4px solid #58a6ff; padding: 8px 16px; color: #8b949e; margin: 16px 0; background: #161b22; border-radius: 0 4px 4px 0; }}
  table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
  th {{ background: #21262d; color: #e6edf3; padding: 10px 14px; text-align: left; border: 1px solid #30363d; }}
  td {{ padding: 8px 14px; border: 1px solid #30363d; }}
  tr:nth-child(even) {{ background: #161b22; }}
  ul, ol {{ padding-left: 24px; margin: 12px 0; }}
  li {{ margin: 4px 0; }}
  hr {{ border: none; border-top: 1px solid #30363d; margin: 24px 0; }}
  img {{ max-width: 100%; border-radius: 8px; border: 1px solid #30363d; margin: 12px 0; }}
  .badge {{ display: inline-block; background: #21262d; color: #58a6ff; border: 1px solid #30363d; border-radius: 20px; padding: 2px 10px; font-size: 12px; margin: 2px; }}
</style>
</head>
<body>
<div class="sidebar">
  <h2>📚 REVD Docs</h2>
  <div class="section">
    <div class="section-title">Navigation</div>
    <a href="/">🏠 Home</a>
    <a href="/SUMMARY.md">📋 Summary</a>
    <a href="/SETUP-GUIDE.md">🔧 Setup Guide</a>
  </div>
  <div class="section">
    <div class="section-title">Projects</div>
    <a href="/01-POS-SUPPLIER-REVD/README.md">1️⃣ POS Supplier</a>
    <a href="/01-POS-SUPPLIER-REVD/FEATURES.md">&nbsp;&nbsp;↳ Features</a>
    <a href="/02-REVDWABOT/README.md">2️⃣ REVD WA Bot</a>
    <a href="/02-REVDWABOT/FEATURES.md">&nbsp;&nbsp;↳ Features</a>
    <a href="/03-ABSENSIQR-REVD/README.md">3️⃣ Absensi QR</a>
    <a href="/03-ABSENSIQR-REVD/FEATURES.md">&nbsp;&nbsp;↳ Features</a>
    <a href="/04-PROJECT-WEB-CLC/README.md">4️⃣ Project Web CLC</a>
    <a href="/04-PROJECT-WEB-CLC/FEATURES.md">&nbsp;&nbsp;↳ Features</a>
  </div>
</div>
<div class="main">
  <div class="content">
    {content}
  </div>
</div>
<script>
  const path = window.location.pathname;
  document.querySelectorAll('.sidebar a').forEach(a => {{
    if (a.getAttribute('href') === path) a.classList.add('active');
  }});
</script>
</body>
</html>"""


class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path)

        # Serve root as index.html
        if path == "/" or path == "":
            fs_path = Path("./index.html")
            try:
                content = fs_path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(500, str(e))
            return

        # Build filesystem path
        fs_path = Path(".") / path.lstrip("/")

        # If directory, try index files
        if fs_path.is_dir():
            for candidate in ["README.md", "index.md"]:
                candidate_path = fs_path / candidate
                if candidate_path.exists():
                    fs_path = candidate_path
                    break

        # Serve markdown files as HTML
        if fs_path.suffix.lower() == ".md" and fs_path.exists():
            try:
                content_md = fs_path.read_text(encoding="utf-8")
                # Fix relative image paths for browser
                content_html = markdown.markdown(
                    content_md,
                    extensions=["tables", "fenced_code", "toc", "nl2br"]
                )
                title = fs_path.stem.replace("-", " ").replace("_", " ").title()
                html = HTML_TEMPLATE.format(title=title, content=content_html)
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
            except Exception as e:
                self.send_error(500, str(e))
        elif fs_path.exists():
            # Serve static files (images, etc.)
            super().do_GET()
        else:
            self.send_error(404, f"File not found: {path}")

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((HOST, PORT), MarkdownHandler) as httpd:
        print(f"Serving REVD Documentation at http://{HOST}:{PORT}")
        httpd.serve_forever()
