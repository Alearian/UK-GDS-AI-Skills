import re
import os
import sys

def clean_md(raw_md, is_home=False):
    lines = raw_md.split('\n')
    start_idx = 0

    if is_home:
        for i, line in enumerate(lines):
            if line.startswith('# Design your service') and i > 20:
                start_idx = i
                break
    else:
        for i, line in enumerate(lines):
            if line.strip().startswith('1. [Home]'):
                start_idx = i
                # Skip breadcrumb lines
                while start_idx < len(lines) and (lines[start_idx].strip().startswith('1.') or lines[start_idx].strip().startswith('2.') or lines[start_idx].strip().startswith('3.') or lines[start_idx].strip() == ''):
                    start_idx += 1
                break

    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == '## Support links':
            end_idx = i
            break

    content = '\n'.join(lines[start_idx:end_idx]).strip()

    base = 'https://design-system.service.gov.uk'
    def convert_link(match):
        text = match.group(1)
        url = match.group(2)
        if url.startswith(base):
            path = url[len(base):]
            if not path or path == '/':
                return f'[{text}](./index.md)'
            path = path.strip('/')
            return f'[{text}](./{path}.md)'
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\((https://design-system\.service\.gov\.uk[^)]*)\)', convert_link, content)
    content = re.sub(r'\[ \]\([^)]*#top\)', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip() + '\n'

# The raw markdown content will be passed via files
base_dir = 'D:/Source/FurnissSoftware/MCPs/GDS/docs'

# Read each saved raw file and process
pages = {
    'index.md': ('home', True),
    'get-started/index.md': ('get-started', False),
    'styles/index.md': ('styles', False),
    'components/index.md': ('components', False),
    'patterns/index.md': ('patterns', False),
    'community/index.md': ('community', False),
}

for filepath, (name, is_home) in pages.items():
    raw_path = os.path.join(base_dir, f'_raw_{name}.md')
    if os.path.exists(raw_path):
        with open(raw_path, 'r', encoding='utf-8') as f:
            raw = f.read()
        cleaned = clean_md(raw, is_home)
        out_path = os.path.join(base_dir, filepath)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f'Written: {out_path}')
        os.remove(raw_path)
    else:
        print(f'Missing raw file: {raw_path}')
