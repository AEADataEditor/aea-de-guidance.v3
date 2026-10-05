#!/usr/bin/env python3
"""Keep the top menu and footer consistent with the main AEA Data Editor site.

Run by Quarto as a ``pre-render`` step (see ``_quarto.yml``). It reads, from
https://github.com/AEADataEditor/aeadataeditor.github.io (branch ``main``):

- ``_data/navigation.yml``  -> ``main`` links become the navbar entries
- ``_config.yml``           -> ``footer.links``, ``organization``, license, feed

and rewrites the blocks of ``_quarto.yml`` between the
``# BEGIN generated: ...`` / ``# END generated: ...`` markers.

Links that point to the old ``/aea-de-guidance/`` subsite are mapped to the
pages of this site; all other site-relative links are made absolute, so they
work wherever this site is served (including PR previews).

Usage: sync_chrome.py [--source DIR]   (DIR: local checkout, instead of fetching)
If the source cannot be read, ``_quarto.yml`` is left unchanged.
"""
import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
QUARTO_YML = HERE / "_quarto.yml"
RAW = "https://raw.githubusercontent.com/AEADataEditor/aeadataeditor.github.io/main/"

# Links to the old subsite that now live in this site
LOCAL = {
    "/aea-de-guidance/": "index.qmd",
    "/aea-de-guidance/index.html": "index.qmd",
    "/aea-de-guidance/FAQ.html": "faq.qmd",
    "/aea-de-guidance/faq.html": "faq.qmd",
}
THIS_REPO = "https://github.com/AEADataEditor/aea-de-guidance.v3"
# Not in _config.yml: hard-coded in the main site's footer.html
EXTRA_FOOTER = [("Disclosures", "/disclosures.html")]
FEED_DEFAULT = "/feed.xml"


def read(name, source):
    if source:
        return (Path(source) / name).read_text(encoding="utf-8")
    with urllib.request.urlopen(RAW + name, timeout=30) as r:
        return r.read().decode("utf-8")


def q(text):
    """Double-quoted YAML scalar."""
    return json.dumps(text, ensure_ascii=False)


def absolute(url, base):
    return base.rstrip("/") + url if url.startswith("/") else url


def navbar_block(nav, base):
    out = []
    for link in nav["main"]:
        url = link["url"]
        href = LOCAL.get(url) or absolute(url, base)
        out += [f"- text: {q(link['title'].strip())}", f"  href: {q(href)}"]
    return out


def footer_block(cfg, base):
    org = cfg.get("organization") or cfg.get("title")
    links = [f"[{t}]({absolute(u, base)})" for t, u in EXTRA_FOOTER]
    links += [f"[{l['label']}]({l['url']})" for l in cfg.get("footer", {}).get("links", []) if l.get("label") and l.get("url")]
    feed = (cfg.get("atom_feed") or {}).get("path") or FEED_DEFAULT
    links.append(f"[Feed]({absolute(feed, base)})")
    copyright_ = f"© {datetime.date.today().year} {org}."
    if cfg.get("license_image"):
        img = cfg["license_image"]
        img = img if img.startswith("http") else f"{base}/images/{img}"
        lic = f"[![{cfg.get('license_name', 'License')}]({img}){{fig-alt={q(cfg.get('license_name', 'License'))}}}]({cfg.get('license_url', base)})"
        copyright_ += " " + lic
    suggestions = f"Suggestions and comments: [GitHub]({THIS_REPO}/issues) | [Email](https://www.aeaweb.org/contact)"
    return [
        "page-footer:",
        f"  left: {q(copyright_)}",
        f"  center: {q(' | '.join(links))}",
        f"  right: {q(suggestions)}",
    ]


def replace_block(text, name, lines):
    pattern = re.compile(rf"^(?P<ind>[ ]*)# BEGIN generated: {name}[^\n]*\n.*?^(?P=ind)# END generated: {name}[^\n]*$", re.S | re.M)
    m = pattern.search(text)
    if not m:
        raise SystemExit(f"markers for '{name}' not found in {QUARTO_YML.name}")
    ind = m.group("ind")
    begin = text[m.start():text.index("\n", m.start())]
    end = f"{ind}# END generated: {name} (scripts/sync_chrome.py)"
    body = "\n".join(f"{ind}{l}" for l in lines)
    return text[:m.start()] + f"{begin}\n{body}\n{end}" + text[m.end():]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="local checkout of aeadataeditor.github.io")
    args = ap.parse_args()
    try:
        nav = yaml.safe_load(read("_data/navigation.yml", args.source))
        cfg = yaml.safe_load(read("_config.yml", args.source))
        base = cfg["url"].rstrip("/")
    except Exception as e:  # network down, file moved, ...
        print(f"WARNING: could not read menu/footer from the main site ({e}); keeping _quarto.yml as is", file=sys.stderr)
        return
    text = QUARTO_YML.read_text(encoding="utf-8")
    text = replace_block(text, "navbar-left", navbar_block(nav, base))
    text = replace_block(text, "page-footer", footer_block(cfg, base))
    QUARTO_YML.write_text(text, encoding="utf-8")
    print("Updated navbar and footer from the main site")


if __name__ == "__main__":
    main()
