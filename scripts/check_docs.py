#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'AGENTS.md', 'PROJECT_STATUS.md',
    'docs/architecture.md', 'docs/repositories.md', 'docs/contract-ownership.md',
    'docs/integration-plan.md', 'docs/roadmap.md', 'docs/adr/README.md',
]
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')

def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f'missing required file: {rel}')

errors = []
for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    if not text.endswith('\n'):
        errors.append(f'{md.relative_to(ROOT)}: missing final newline')
    for target in LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        path_part = target.split('#', 1)[0].split('?', 1)[0]
        if not path_part:
            continue
        resolved = (md.parent / path_part).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f'{md.relative_to(ROOT)}: link escapes repo: {target}')
            continue
        if not resolved.exists():
            errors.append(f'{md.relative_to(ROOT)}: broken relative link: {target}')

for forbidden in ['.env', 'id_rsa', 'id_ed25519']:
    if (ROOT / forbidden).exists():
        errors.append(f'forbidden secret-like file exists at repository root: {forbidden}')

if errors:
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    raise SystemExit(1)

print('Repository documentation checks passed.')
