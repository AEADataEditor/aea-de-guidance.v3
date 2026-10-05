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
├── mytheme.scss, styles.css
└── _site/          # generated output (not committed)
```

New pages must be added to the `sidebar` in `_quarto.yml`.

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
- The site is deployed to GitHub Pages by `.github/workflows/quarto-publish.yml` on push to `main`.
