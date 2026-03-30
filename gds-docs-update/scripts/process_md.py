"""
Script to clean raw GDS markdown - strips nav chrome, converts links to relative .md paths.
"""
import re
import sys
import os

def clean_markdown(raw_md: str, current_path: str) -> str:
    """Clean raw GDS markdown by removing navigation chrome and fixing links."""

    # Find the main content - it starts after the last navigation section
    # The main content typically starts with a breadcrumb or heading after the nav

    # Remove cookie banner
    lines = raw_md.split('\n')

    # Find where main content starts - look for the breadcrumb "1. [Home]" or the first h1
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('1. [Home]'):
            start_idx = i + 1
            break

    # If no breadcrumb found, look for ## Pages in this section and skip past it
    if start_idx == 0:
        for i, line in enumerate(lines):
            if '# Design your service' in line or (line.startswith('#  ') and i > 50):
                start_idx = i
                break

    # Find where footer starts
    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == '## Support links':
            end_idx = i
            break

    content = '\n'.join(lines[start_idx:end_idx]).strip()

    # Convert absolute GDS links to relative .md links
    base = 'https://design-system.service.gov.uk'

    def convert_link(match):
        text = match.group(1)
        url = match.group(2)
        if url.startswith(base):
            # Convert to relative path
            path = url[len(base):]
            if not path or path == '/':
                rel = './index.md'
            else:
                path = path.strip('/')
                rel = f'./{path}.md'
            return f'[{text}]({rel})'
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\((https://design-system\.service\.gov\.uk[^)]*)\)', convert_link, content)

    # Remove "[ ](url#top)" back-to-top links
    content = re.sub(r'\[ \]\([^)]*#top\)', '', content)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip() + '\n'


def url_to_filepath(url: str, base_dir: str) -> str:
    """Convert a URL to a local file path."""
    base = 'https://design-system.service.gov.uk'
    path = url[len(base):].strip('/')
    if not path:
        return os.path.join(base_dir, 'index.md')
    return os.path.join(base_dir, f'{path}.md')


if __name__ == '__main__':
    import json
    # Read from stdin: {"url": "...", "markdown": "..."}
    data = json.load(sys.stdin)
    url = data['url']
    md = data['markdown']

    base_dir = sys.argv[1] if len(sys.argv) > 1 else 'docs'
    filepath = url_to_filepath(url, base_dir)

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    cleaned = clean_markdown(md, filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f'Written: {filepath}')
