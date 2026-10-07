"""Manage this proposal's GitHub repository and Pages using existing Git credentials.

Credentials stay in process memory; they are never printed or saved in project files.
"""
import argparse
import json
import os
import subprocess
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

OWNER = 'gabi0102souza-stack'
REPO = 'fresta-site'
PREFIX = f'/repos/{OWNER}/{REPO}'

def token():
    environment = dict(os.environ, GCM_INTERACTIVE='never', GIT_TERMINAL_PROMPT='0')
    result = subprocess.run(['git', 'credential', 'fill'],
        input=f'protocol=https\nhost=github.com\nusername={OWNER}\n\n',
        text=True, capture_output=True, env=environment, check=False)
    values = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    if result.returncode or not values.get('password'):
        raise RuntimeError('Existing GitHub credential unavailable; no credential was printed.')
    return values['password']

def api(method, path, body=None):
    request = Request('https://api.github.com' + path,
        data=json.dumps(body).encode() if body is not None else None,
        method=method,
        headers={'Authorization': 'Bearer ' + TOKEN,
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json', 'User-Agent': 'Fresta-preview-publisher'})
    try:
        with urlopen(request, timeout=30) as response:
            payload = response.read()
            return response.status, json.loads(payload) if payload else {}
    except HTTPError as error:
        payload = json.loads(error.read().decode())
        return error.code, {'message': payload.get('message'), 'errors': payload.get('errors')}

def emit(label, result):
    status, payload = result
    fields = ('message', 'errors', 'login', 'id', 'name', 'full_name', 'html_url',
        'private', 'default_branch', 'size', 'permissions', 'status', 'build_type', 'source')
    print(json.dumps({'step': label, 'http_status': status,
        **{key: payload[key] for key in fields if key in payload}}, ensure_ascii=False))
    return status, payload

parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['inspect', 'create-repo', 'enable-pages', 'status', 'dispatch'])
args = parser.parse_args()
try:
    TOKEN = token()
    status, user = emit('authenticated user', api('GET', '/user'))
    if status != 200 or user.get('login', '').lower() != OWNER.lower():
        raise RuntimeError('Authenticated account does not match the intended owner.')
    if args.action == 'inspect':
        emit('repository', api('GET', PREFIX))
        emit('pages', api('GET', PREFIX + '/pages'))
    elif args.action == 'create-repo':
        status, existing = api('GET', PREFIX)
        if status == 404:
            status, _ = emit('create repository', api('POST', '/user/repos', {
                'name': REPO, 'description': 'Proposta de site para Fresta, Pinheiros. Preview conceitual.',
                'private': False, 'auto_init': False, 'has_issues': False, 'has_wiki': False}))
            if status != 201: sys.exit(1)
        elif status == 200:
            emit('repository already exists', (status, existing))
        else:
            emit('repository lookup failed', (status, existing)); sys.exit(1)
    elif args.action == 'enable-pages':
        status, existing = api('GET', PREFIX + '/pages')
        if status == 404:
            status, _ = emit('enable Pages workflow', api('POST', PREFIX + '/pages', {'build_type': 'workflow'}))
            if status != 201: sys.exit(1)
        elif status == 200:
            emit('existing Pages', (status, existing))
            if existing.get('build_type') != 'workflow':
                status, _ = emit('set workflow build', api('PUT', PREFIX + '/pages', {'build_type': 'workflow'}))
                if status != 204: sys.exit(1)
        else:
            emit('Pages lookup failed', (status, existing)); sys.exit(1)
    elif args.action == 'dispatch':
        status, _ = emit('dispatch Pages', api('POST', PREFIX + '/actions/workflows/pages.yml/dispatches', {'ref': 'main'}))
        if status != 204: sys.exit(1)
    elif args.action == 'status':
        emit('pages', api('GET', PREFIX + '/pages'))
        status, runs = api('GET', PREFIX + '/actions/runs?per_page=5')
        print(json.dumps({'step': 'workflow runs', 'http_status': status,
            'runs': [{key: run.get(key) for key in ('id', 'name', 'head_sha', 'status', 'conclusion', 'html_url')}
                for run in runs.get('workflow_runs', [])]}, ensure_ascii=False))
except Exception as error:
    print(str(error), file=sys.stderr)
    sys.exit(1)
