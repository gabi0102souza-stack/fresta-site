"""Check every rendered local asset under the GitHub Pages subpath."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlparse
import re
import struct
import json
import argparse

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:4173/fresta-site/')
parser.add_argument('--output', default='qa/http-results.json')
args = parser.parse_args()
BASE = args.base_url.rstrip('/') + '/'
document = (DIST / 'index.html').read_text(encoding='utf-8')
references = set(re.findall(r'(?:href|src)="([^"]+)"', document))
references.update(re.findall(r'url\([\'"]?([^\)\'\"]+)', (DIST / 'styles.css').read_text(encoding='utf-8')))
references = {r for r in references if not r.startswith('#') and not urlparse(r).scheme}
references.update({'','og-fresta.png'})
results = []
for reference in sorted(references):
    with urlopen(BASE + reference, timeout=10) as response:
        payload = response.read()
        if reference.endswith('.woff2'): assert payload[:4] == b'wOF2', reference
        if reference == 'og-fresta.png': assert struct.unpack('>II', payload[16:24]) == (1200,630)
        assert response.status == 200, reference
        results.append({'path':reference or 'index.html','status':response.status,'bytes':len(payload)})
(ROOT / args.output).write_text(json.dumps(results,indent=2),encoding='utf-8')
print(f'PASS: {len(results)} requests, all 200 at {BASE}. WOFF2 signatures and OG dimensions valid.')
