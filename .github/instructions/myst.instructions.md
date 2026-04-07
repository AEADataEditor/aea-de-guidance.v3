---
description: "Use when: editing MyST markdown files, modifying myst.yml, working with MyST directives, updating table of contents, adding pages to navigation, using grid/card layouts, working with dropdown components, MyST syntax, MyST configuration, MyST documentation, Jupyter Book"
applyTo:
  - "website/**/*.md"
  - "website/myst.yml"
---

# MyST (Markedly Structured Text) Documentation Project

This is a MyST-based documentation website. MyST is an extended markdown syntax that adds powerful features for technical documentation.

## Project Structure

- **Configuration**: `website/myst.yml` - main MyST configuration file
- **Content**: `website/*.md` - markdown content files
- **Build output**: `website/_build/` - generated HTML (do not edit)
- **Development server**: `jupyter book start` (from website directory)

## MyST Syntax Patterns Used in This Project

### YAML Frontmatter

All content files start with YAML frontmatter between `---` markers:

```yaml
---
title: Page Title
toc: true  # Show table of contents
site:
  hide_outline: true
  hide_toc: true
  hide_title_block: true
---
```

### Colon Fence Directives

MyST uses colon fences for directives. The number of colons indicates nesting level:

```markdown
::::{grid} 1 1 2 3
:::{card}
:link: /step-1
**Title**
^^^
Content here
+++
Footer text »
:::
::::
```

**Key directives in this project:**
- `::::{grid}` - Create responsive grid layouts
- `:::{grid-item-card}` - Card within a grid
- `:::{card}` - Standalone card with header/body/footer
- `````{dropdown}` - Collapsible content sections

### Card Directive Structure

Cards can be structured in multiple ways. This project uses the `^^^` and `+++` marker syntax:

**Standard syntax in this project (using markers):**
```markdown
:::{card} 
:link: /page-url
**Title Text**
^^^ 
Body content with images and text
+++ 
**Footer text** »
:::
```

- **Title**: Everything before `^^^`
- **Body**: Between `^^^` and `+++`  
- **Footer**: After `+++`
- **Link option**: `:link:` - Makes entire card clickable

**Alternative MyST syntax (using options):**
```markdown
:::{card} Card Title
:link: /page-url
:header: Header text with **markdown**
:footer: Footer text

Body content goes here (this is the main directive body)
:::
```

**Prefer the marker syntax (`^^^`/`+++`) for consistency with existing files in this project.**

### Plus Fence Syntax (`+++`)

`+++` has two uses:

1. **Within cards** - As a separator between body and footer (as shown above)
2. **As a metadata block** - To attach attributes to content:

```markdown
+++ { "class": "col-body-outset" }
Content here with special styling
+++
```

### Enabled Extensions

This project has these MyST extensions enabled (see `myst.yml`):

- `colon_fence` - Required for `:::` blocks
- `deflist` - Definition lists
- `html_admonition` - Note/warning boxes
- `html_image` - Advanced image options
- `linkify` - Auto-convert URLs to links
- `substitution` - Variable substitution
- `tasklist` - Checkbox lists
- `fieldlist` - Field lists
- `cards` - Card directives

## Editing myst.yml

### Table of Contents (TOC) Structure

The `project.toc` section defines navigation. Each entry can be:

**Simple file reference:**
```yaml
- file: index.md
```

**Section with children:**
```yaml
- title: Step 1 - Prepare
  file: step-1.md
  children:
    - file: preparing-for-data-deposit.md
    - file: sharing-restricted-data.md
```

**External link:**
```yaml
- title: Step 3 - Submit
  url: https://www.aeaweb.org/journals
```

### Important TOC Rules

1. **File paths** are relative to the `website/` directory
2. **No file extensions** in most contexts - use `file: index.md` not `file: index`
3. **Indentation matters** - use 2 spaces for nested items
4. **Comment syntax** - Use `#` for comments (e.g., `#- file: draft.md`)
5. **Children must be indented** under the parent with proper spacing

### Navigation Bar

The `site.nav` section defines top-level navigation:

```yaml
site:
  nav:
    - title: "START REPLICATION PACKAGE"
      url: /index
    - title: "FAQ"
      url: /faq
```

## Common Tasks

### Adding a New Page

1. Create the markdown file in `website/`
2. Add YAML frontmatter with at least a `title`
3. Add entry to `myst.yml` TOC:
   ```yaml
   - file: new-page.md
   ```
   Or as a child under an existing section

### Creating a Card Grid Layout

```markdown
::::{grid} 1 1 2 3
:::{card}
:link: /page1
**Card 1 Title**
^^^
Description text
+++
Action link »
:::

:::{card}
:link: /page2
**Card 2 Title**
^^^
Description text
+++
Action link »
:::
::::
```

Grid parameters: `{grid} mobile tablet desktop wide`

### Adding a Dropdown

Dropdowns are collapsible content sections:

```markdown
````{dropdown} **Click to expand**
Content that starts collapsed
````
```

Options:
- `:open:` - Start in expanded state
- Use 4 backticks when dropdown contains code blocks with 3 backticks

### Other Useful Directives

**Admonitions** (notes, warnings, tips):
```markdown
:::{note}
This is an important note!
:::

:::{warning}
Be careful with this!
:::
```

Available types: `note`, `tip`, `warning`, `important`, `caution`, `danger`

**Inline images with captions:**
```markdown
:::{figure} /images/diagram.png
:width: 80%
:alt: Diagram description

Caption text goes here
:::
```

**Code blocks with syntax highlighting:**
```markdown
```{code-block} python
:linenos:
:emphasize-lines: 2,3

def hello():
    print("Hello")
    return True
\```
```

## File Naming Conventions

- Use lowercase with hyphens: `preparing-for-data-deposit.md`
- Be descriptive: `step-1.md`, not `s1.md`
- Match TOC entry: if TOC says `file: step-1.md`, file must be `step-1.md`

## Best Practices

1. **Always include frontmatter** with at least a title
2. **Test TOC changes** - incorrect YAML breaks the build
3. **Use consistent heading levels** - start with `##` (since `title` becomes `#`)
4. **Close all directives** - every `::::{grid}` needs `::::`
5. **Match colon counts** - opening `::::` must close with `::::`
6. **Quote titles with colons** in YAML - `title: "Step 1: Prepare"`
7. **Relative links** use `/` prefix: `[text](/other-page)` not `[text](other-page.md)`

## Common Mistakes to Avoid

❌ **Missing file in TOC entry:**
```yaml
- file: nonexistent.md  # Will cause build error
```

❌ **Mismatched colons:**
```markdown
::::{grid}
:::{card}
:::  # Missing fourth colon
```

❌ **Wrong indentation in TOC:**
```yaml
- title: Parent
  children:
  - file: child.md  # Should be indented 2 more spaces
```

❌ **Tabs instead of spaces** in YAML (must use spaces)

## Build and Preview

From the `website/` directory:

```bash
# Start development server
jupyter book start

# Build static site
jupyter book build
```

## Documentation References

- MyST Guide: https://mystmd.org/guide
- MyST Syntax Overview: https://mystmd.org/guide/syntax-overview
- MyST Frontmatter: https://mystmd.org/guide/frontmatter
- Directives Reference: https://mystmd.org/guide/directives
- Cards and Grids: https://mystmd.org/guide/dropdowns-cards-and-tabs

## When Helping with This Project

- Always validate YAML syntax when editing `myst.yml`
- Check that files referenced in TOC actually exist
- Preserve existing formatting patterns (especially `^^^`/`+++` card markers)
- Test that links use the project's link format (relative paths with `/`)
- Remember: This builds a static site, so all navigation must be in `myst.yml`
- Use the marker syntax (`^^^`/`+++`) for cards to match project conventions
- Ensure proper indentation in YAML (2 spaces, never tabs)
