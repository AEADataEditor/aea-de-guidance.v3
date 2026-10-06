# Deployment & PR previews

This repo's site is built with [Quarto](https://quarto.org/) and published to
GitHub Pages via [.github/workflows/quarto-publish.yml](.github/workflows/quarto-publish.yml).
The setup follows the one at
[aeadataeditor.github.io](https://github.com/AEADataEditor/aeadataeditor.github.io/blob/main/README-DEPLOYMENT.md),
except that this site publishes with GitHub Pages (Actions) rather than a
`gh-pages` branch. The workflow has three jobs:

- **build** — always runs (push to `main`, pull requests, manual dispatch).
  Renders the Quarto site and uploads it as a workflow artifact named `site`
  (kept 14 days, so a PR's rendered site can be downloaded).
- **deploy** — runs on pushes to `main` (or a manual dispatch with
  "deploy" set to `true`). Publishes to GitHub Pages. Repository setting
  *Settings → Pages → Source* must be **GitHub Actions**.
- **preview** — runs on pull requests opened from a branch of this
  repository (not a fork). Deploys the `site` artifact to
  [Cloudflare Pages](https://pages.cloudflare.com/) as a per-PR preview,
  then posts (or updates) a comment on the PR with the preview link.

Forked PRs never run the `preview` job's deploy step, since forks don't have
access to repository secrets — that's a GitHub Actions security boundary,
not a bug.

## One-time Cloudflare Pages setup

You need a Cloudflare account and an API token before the `preview` job can
deploy anything. If the same Cloudflare account is used as for
aeadataeditor.github.io, reuse its token and account ID.

1. **Create the Cloudflare API token.**
   In the Cloudflare dashboard: **My Profile → API Tokens → Create Token**,
   using the **"Edit Cloudflare Workers"** template (or a custom token with
   `Account.Cloudflare Pages: Edit` permission). Copy the token value — it's
   only shown once.

2. **Find your Cloudflare Account ID.**
   It's shown on the right-hand sidebar of any zone/domain overview page in
   the Cloudflare dashboard, or via `wrangler whoami`.

3. **Set both as GitHub Actions secrets on this repo:**

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN --repo AEADataEditor/aea-de-guidance.v3
   gh secret set CLOUDFLARE_ACCOUNT_ID --repo AEADataEditor/aea-de-guidance.v3
   ```

4. **Create the Cloudflare Pages project**, if it doesn't already exist.
   The workflow deploys to a project named `aea-de-guidance-v3`
   (the `PREVIEW_PROJECT` variable at the top of the workflow). Create it once with
   [Wrangler](https://developers.cloudflare.com/workers/wrangler/):

   ```bash
   npx wrangler login
   npx wrangler pages project create aea-de-guidance-v3
   ```

   Otherwise, `wrangler pages deploy` in CI will create the project
   automatically on the first PR.

5. **Verify the secrets are set:** `gh secret list --repo AEADataEditor/aea-de-guidance.v3`

## After setup

Every PR from a repo branch (not a fork) will get:

- A live preview at a Cloudflare Pages URL specific to that PR
  (`https://pr-<PR number>.aea-de-guidance-v3.pages.dev`), rebuilt on every
  push to the PR.
- A site built with `site-url` set to that preview URL, so absolute links stay
  on the preview instead of pointing at production.
- A PR comment with the preview link, edited in place on each new commit
  rather than re-posted.

Until the secrets exist, the `preview` job's deploy step fails on PRs; the
`build` job and its downloadable `site` artifact are unaffected.

## Previewing locally

```bash
quarto preview website
```

## Changing the project name

If you rename the Cloudflare Pages project, update `PREVIEW_PROJECT` in
[.github/workflows/quarto-publish.yml](.github/workflows/quarto-publish.yml).
