# Developing this site

This site uses MyST (Markedly Structured Text) via Jupyter Book to build documentation with dynamic content.

## Setup

Create a Python environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Building the Site

### Development Server

Run the live development server (auto-rebuilds on file changes):

```bash
cd website
jupyter book start
```

The site will be available at `http://localhost:3000`.

### Build Static HTML

Build the complete site:

```bash
cd website
python generate_faq_cards.py  # Generate FAQ cards
jupyter book build
```

Or using `myst` directly:

```bash
cd website
python generate_faq_cards.py  # Generate FAQ cards
myst build
```

**Important:** Run `generate_faq_cards.py` before building to regenerate the FAQ card grid from the individual FAQ files in `faq/`.

### Quick Build (Development)

For faster builds during development (if you haven't changed FAQ content):

```bash
cd website
jupyter book build
```

## Project Structure

```
website/
├── myst.yml              # MyST configuration and table of contents
├── *.md                  # Main content pages
├── faq/                  # Individual FAQ pages (auto-listed)
│   └── *.md
├── images/               # Static assets
└── _build/               # Generated output (not committed)
    └── html/
```

## Dynamic Content

The FAQ landing page (`faq.md`) uses a preprocessing script to:
- Automatically scan all files in `faq/` directory
- Parse frontmatter (title, tags) from each FAQ
- Generate `faq-include.md` with a responsive card grid layout
- Update automatically when FAQ files are added/removed

To add a new FAQ:
1. Create a new `.md` file in `website/faq/`
2. Add frontmatter with `title` and `tags`
3. Add the file to `myst.yml` under `faq.md` children
4. Run `python generate_faq_cards.py` to regenerate cards
5. Rebuild the site

## Testing

### Manual Testing
Generate FAQ cards:**
   ```bash
   cd website
   python generate_faq_cards.py
   ```

2. **Local build test:**
   ```bash
   cd website
   jupyter book build
   ```

3. **Check for errors:**
   - Look for build errors in the terminal output
   - Check `_build/html/` directory was created
   - Verify `faq-include.md` was generated and contains card markup

4. **Visual testing:**
   ```bash
   cd website
   jupyter book start
   ```
   Navigate to `/faq` and verify:
   - All FAQ cards appear
   - Cards are clickable and link to correct pages
   - Card layout is responsive

### Automated Testing (CI/CD)

The GitHub Actions workflow automatically:
- Installs dependencies from `requirements.txt`
- Run `python generate_faq_cards.py` from the `website/` directory
- Check that `faq-include.md` was generated
- Verify FAQ files are in `website/faq/` and listed in `myst.yml`

**Build errors:**
- Check YAML syntax in FAQ file frontmatter
- Ensure all required packages are in `requirements.txt`
- Verify frontmatter YAML is valid in all `.md` files
- Check that `faq-include.md` contains valid MyST card syntax

**Links broken:**
- Use relative paths with `/` prefix: `/faq/page-name`
- Match filenames exactly (case-sensitive)
- Check TOC entries in `myst.yml`

## AI Assistant Instructions

When working with this codebase:
- Run `python generate_faq_cards.py` before building if FAQ files changed
- FAQ pages must be added to both `website/faq/` AND `myst.yml` TOC
- Use the MyST instructions file at `.github/instructions/myst.instructions.md`
- Test builds locally before committing
- Verify the GitHub Actions workflow passes
- The preprocessing script must be run before each build when FAQ content chang
## AI Assistant Instructions

When working with this codebase:
- Always build with `--execute` flag when FAQ or dynamic content changes
- FAQ pages must be added to both `website/faq/` AND `myst.yml` TOC
- Use the MyST instructions file at `.github/instructions/myst.instructions.md`
- Test builds locally before committing
- Verify the GitHub Actions workflow passes

## Additional Resources

- [MyST Documentation](https://mystmd.org/guide)
- [Jupyter Book Documentation](https://jupyterbook.org/)
- [MyST Instructions](.github/instructions/myst.instructions.md)

