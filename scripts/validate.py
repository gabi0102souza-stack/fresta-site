"""Structural HTML, local assets, fragments and delivery checks (standard library)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.references, self.ids, self.links = [], [], [], set(), []
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1': self.h1 += 1
        if tag == 'html' and attrs.get('lang') != 'pt-BR': self.errors.append('Incorrect language')
        if 'id' in attrs:
            if attrs['id'] in self.ids: self.errors.append(f'Duplicate id: {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'img':
            if 'alt' not in attrs: self.errors.append('Missing image alternative')
            if not attrs.get('width') or not attrs.get('height'): self.errors.append('Unreserved image size')
        if attrs.get('target') == '_blank' and 'noopener' not in attrs.get('rel',''): self.errors.append('Unsafe blank target')
        for attribute in ('href','src'):
            if attribute in attrs:
                self.references.append(attrs[attribute])
                if tag == 'a' and attribute == 'href': self.links.append(attrs[attribute])
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in VOID: return
        if not self.stack or self.stack[-1] != tag: self.errors.append(f'Invalid tag nesting at </{tag}>')
        else: self.stack.pop()

audit = Audit()
document = (DIST / 'index.html').read_text(encoding='utf-8')
audit.feed(document)
if audit.stack: audit.errors.append(f'Unclosed tags: {audit.stack}')
if audit.h1 != 1: audit.errors.append(f'Expected one H1, got {audit.h1}')
if 'noindex,nofollow' not in document: audit.errors.append('Missing proposal robots setting')
for reference in audit.references:
    if reference.startswith('#'):
        if reference[1:] not in audit.ids: audit.errors.append(f'Broken fragment: {reference}')
    elif not urlparse(reference).scheme:
        if reference.startswith('/'): audit.errors.append(f'Root-relative reference: {reference}')
        if not (DIST / unquote(urlparse(reference).path)).is_file(): audit.errors.append(f'Missing asset: {reference}')
styles = (DIST / 'styles.css').read_text(encoding='utf-8')
for reference in re.findall(r'url\([\'"]?([^\)\'\"]+)', styles):
    if urlparse(reference).scheme: audit.errors.append(f'External CSS asset: {reference}')
    elif not (DIST / reference).is_file(): audit.errors.append(f'Missing CSS asset: {reference}')
for reference in audit.links:
    if urlparse(reference).scheme and not reference.startswith('https://'): audit.errors.append(f'Unexpected external protocol: {reference}')
for required in ('favicon.png','og-fresta.png','.nojekyll'):
    if not (DIST / required).exists(): audit.errors.append(f'Missing delivery file: {required}')
if audit.errors:
    print('\n'.join(audit.errors)); sys.exit(1)
print(f'PASS: valid nesting, one H1, {len(audit.ids)} unique ids, {len(audit.references)} HTML references, CSS assets, fragments, proposal metadata.')
print(f'Delivery: {sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file()):,} bytes. No build dependencies.')
print('External destinations:')
for link in sorted(set(link for link in audit.links if link.startswith('https://'))): print(link)
