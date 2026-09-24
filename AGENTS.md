# AGENTS.md

Personal portfolio/blog "Benny's Blog" — a React 19 + Vite static site deployed to GitHub Pages at `https://Mcc-Mak.github.io/blog/`.

## Commands

- `npm run dev` — dev server
- `npm run build` — Vite build to `dist/`
- `npm run lint` — ESLint (`eslint .`)
- `npm run deploy` — runs `predeploy` (build) then `gh-pages -d dist`
- No tests, no typecheck. Verify changes with `npm run lint` then `npm run build`.
- `npm install` works via the repo-local `.npmrc` (`legacy-peer-deps=true`); `eslint-plugin-react-hooks@4` is pinned because its peer range predates ESLint 9. `eslint.config.js` attaches the react-hooks rules manually and enables `react/jsx-uses-vars`.

## Changelog & commit convention (required for every change)

For every code or content change, before finishing:

1. Update `CHANGELOG.md` — bump the version (semver `X.X.X`), add a dated entry describing the change (Keep a Changelog style: Added / Changed / Fixed / Removed).
2. `git commit` with a clear subject line and a body explaining what changed and why.
3. Work on `dev-001`: `.github/workflows/auto_merge.yml` auto-merges `dev-001 → dev → main` on push. Do not push to `main` directly.

## Deploy workflow

Deploy order matters: commit + push to `dev-001` first (it auto-merges through `dev` to `main`), then `npm run deploy` (this is what README.md documents). `deploy` publishes the static build to the `gh-pages` branch (not `main` or `docs/`).

## Path base quirk (do not "fix")

Administered under the `/blog/` subpath at runtime:
- `vite.config.js` sets `base: '/blog/'`
- `app.jsx` uses `<BrowserRouter basename="/blog">`

Use `import.meta.env.BASE_URL` (e.g. `${import.meta.env.BASE_URL}img/benny.png`) for any asset/markdown public paths, as `src/pages/home.jsx` does. Literal absolute paths like `/img/...` in markdown break under `/blog/`.

## Gallery

`/gallery` (see `src/pages/gallery.jsx`) renders accordion sections parsed from `public/gallery.md` — each `## ` heading becomes one collapsible block. Content is fetched at runtime from `public/` and is the live source of truth.

## `projects/` (portfolio content)

Source code only, grouped by category and named with lowercase `[a-z0-9_.]`. Exception: the canonical root docs keep their conventional uppercase names — `AGENTS.md`, `LICENSE`, `README.md`, `CHANGELOG.md` (and per-project `LICENSE`/`README.md`).

```
projects/trading/{automated_trading_robot,us_stock_scanner}
projects/robotics/{jenga_ur_robot,sound_processing}
projects/computer_vision/{face_point_detector_68,image_processing_tools}
projects/embedded_iot/m5stack
projects/web/personal_web
projects/games/{skywar,treasury_hunter_ios}
projects/algorithms/python_basic_algorithms
```

- Each project's nested `.git/` and `README.md` were removed; original repos stay on GitHub (`chunwmak9/<name>`) and are linked as the `source` in `src/data/projects.js`.
- Do not commit venvs, `__pycache__/`, `*.pyc`, `.DS_Store`, `db.sqlite3`, PyInstaller `build/` output (see `.gitignore`).

## Project showcase wiring

Three views of the same portfolio must stay in sync:

1. `src/data/projects.js` — single source of truth for cards/tags (name, category, role tags, tech, run command, media, source link). Edit here first.
2. Root `README.md` — toctree grouped by the same categories; entries link to `projects/<category>/<slug>/` and images to `public/projects/<slug>/`.
3. `public/projects/<slug>/` — showcase screenshots/demos referenced by both the site (`${import.meta.env.BASE_URL}projects/<slug>/...`) and the README (`public/projects/<slug>/...`). Game sprites and runtime assets stay inside `projects/<slug>/` where the code expects them.