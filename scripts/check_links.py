#!/usr/bin/env python3
"""Check the links in this repo's Markdown files.

Offline (the default) checks that:
  - every relative link points to a file inside the repo,
  - every web link uses https, and prepnplaced.com links use the www host,
  - no Markdown file uses an em dash (house style).

--online also fetches each linked page once and checks that every #anchor a
link jumps to still exists on that page. Question anchors on prepnplaced.com
are built from the question's wording, so a reworded question shows up here.

Exits 0 when everything passes and 1 otherwise. Python 3.9+, standard library only.
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# [text](target). Link text may contain escaped characters such as \* or \[.
LINK = re.compile(r"\[(?:\\.|[^\]\\])*\]\(([^)\s]+)\)")
EM_DASH = "—"
TIMEOUT_SECONDS = 20
USER_AGENT = "prepnplaced-oss-link-check/1.0 (+https://www.prepnplaced.com)"


def markdown_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_offline(path, text):
    """Return (problems, links) for one Markdown file."""
    problems = []
    if EM_DASH in text:
        problems.append("contains an em dash; use a colon, comma or full stop")
    links = LINK.findall(text)
    for target in links:
        if target.startswith("http://"):
            problems.append(f"not https: {target}")
        elif target.startswith("https://prepnplaced.com"):
            problems.append(f"use https://www.prepnplaced.com: {target}")
        elif target.startswith(("https://", "mailto:", "#")):
            continue
        else:
            local = (path.parent / target.split("#", 1)[0]).resolve()
            if local != ROOT and ROOT not in local.parents:
                problems.append(f"points outside the repo: {target}")
            elif not local.exists():
                problems.append(f"missing file: {target}")
    return problems, links


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.read().decode("utf-8", "replace")


def check_online(urls):
    """Fetch each page once; report pages that fail and anchors that are gone."""
    anchors_by_page = {}
    for url in urls:
        page, _, anchor = url.partition("#")
        page = page.split("?", 1)[0]  # tracking parameters do not change the page
        anchors = anchors_by_page.setdefault(page, set())
        if anchor:
            anchors.add(anchor)
    problems = []
    for page in sorted(anchors_by_page):
        try:
            html = fetch(page)
        except (urllib.error.URLError, OSError) as error:
            problems.append(f"{page}: {error}")
            continue
        for anchor in sorted(anchors_by_page[page]):
            if f'id="{anchor}"' not in html:
                problems.append(f"{page}#{anchor}: anchor not found on the page")
    return problems


def main():
    parser = argparse.ArgumentParser(description="Check the links in this repo's Markdown files.")
    parser.add_argument("--online", action="store_true", help="also fetch every linked page and check its anchors")
    args = parser.parse_args()

    files = markdown_files()
    problems = []
    web_links = set()
    total_links = 0
    for path in files:
        file_problems, links = check_offline(path, path.read_text(encoding="utf-8"))
        total_links += len(links)
        problems += [f"{path.relative_to(ROOT)}: {problem}" for problem in file_problems]
        web_links.update(link for link in links if link.startswith("https://"))
    if args.online:
        problems += check_online(web_links)

    for problem in problems:
        print(problem)
    mode = "online" if args.online else "offline"
    print(f"{len(files)} files, {total_links} links ({len(web_links)} unique web links), {len(problems)} problems [{mode}]")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
