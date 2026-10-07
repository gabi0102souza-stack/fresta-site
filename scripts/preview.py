"""Local preview at the same subpath as GitHub Pages. No dependencies."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import argparse

ROOT = Path(__file__).resolve().parents[1] / 'dist'

class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        relative = urlparse(path).path.removeprefix('/fresta-site/').lstrip('/')
        candidate = (ROOT / relative).resolve()
        return str(candidate if candidate.is_relative_to(ROOT) else ROOT / 'not-found')

    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/fresta-site/')
            self.end_headers()
            return
        if self.path == '/fresta-site/styles.css?qa=reduce':
            styles = (ROOT / 'styles.css').read_text(encoding='utf-8')
            styles = styles.replace('@media(prefers-reduced-motion:no-preference)', '@media not all').replace('@media(prefers-reduced-motion:reduce)', '@media all')
            payload = styles.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/css; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if self.path == '/fresta-site/?qa=reduce':
            document = (ROOT / 'index.html').read_text(encoding='utf-8').replace('href="styles.css"', 'href="styles.css?qa=reduce"')
            payload = document.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if self.path == '/fresta-site/?qa=nojs':
            document = (ROOT / 'index.html').read_text(encoding='utf-8').replace('<script src="main.js" defer></script>', '')
            payload = document.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    print(f'Fresta preview: http://127.0.0.1:{args.port}/fresta-site/', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), PreviewHandler).serve_forever()
