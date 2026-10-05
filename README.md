# Developing this site

This site is built with [Quarto](https://quarto.org/) (as is the [Social Science Data Editors guidance](https://social-science-data-editors.github.io/guidance/)). It mirrors the `_guidance` section of [aeadataeditor.github.io](https://github.com/AEADataEditor/aeadataeditor.github.io).

## Setup

Install [Quarto](https://quarto.org/docs/get-started/) (or `pip install quarto-cli`).

## Building the site

```bash
quarto preview website   # live development server
quarto render website    # static HTML in website/_site/
```

## Project structure

```
website/
├── _quarto.yml     # navbar, sidebar (table of contents), footer, theme
├── *.qmd           # content pages
├── faq.qmd         # FAQ landing page: searchable grid listing of faq/*.qmd
├── faq/*.qmd       # one file per FAQ
├── images/         # static images
├── scripts/sync_chrome.py  # pre-render: top menu + footer from the main site
├── mytheme.scss, styles.css
└── _site/          # generated output (not committed)
```

New pages must be added to the `sidebar` in `_quarto.yml`.

## Top menu and footer

The top menu and the footer are kept consistent with the main site
([aeadataeditor.github.io](https://github.com/AEADataEditor/aeadataeditor.github.io)).
`website/scripts/sync_chrome.py` runs automatically as a Quarto `pre-render` step. It reads
`_data/navigation.yml` and `_config.yml` from the `main` branch of that repository and rewrites the
blocks between the `# BEGIN generated` / `# END generated` markers in `website/_quarto.yml`
(links to the old `/aea-de-guidance/` subsite are mapped to this site's pages). If the main site
cannot be reached, `_quarto.yml` is left as it is. Commit the updated `_quarto.yml` when it changes.
Use `--source DIR` to read from a local checkout instead.

## FAQ

Each FAQ is a separate file in `website/faq/`. The full question is the `title`; `categories` are keywords. `faq.qmd` displays all FAQs on one page as a grid, with a filter box (searches titles and categories) and a category list. To add a FAQ, simply add a new `.qmd` file to `website/faq/`:

```yaml
---
title: "The full question?"
categories: [keyword one, keyword two]
---

Answer.
```

No other file needs to be changed.

## Conventions

- Link to other pages with root-relative `.qmd` paths: `[text](/data-deposit-aea.qmd#anchor)`. Images: `/images/name.png`.
- Collapsible sections use collapsed callouts: `::: {#id .callout-note collapse="true" icon=false title="Title"}` ... `:::`.
- The site is deployed to GitHub Pages on push to `main`; pull requests get a preview. See [README-DEPLOYMENT.md](README-DEPLOYMENT.md).
