# Changelog

All notable changes to this project are documented here, with a semver version (`X.X.X`) per released change set.

## [1.8.0] - 2026-09-25

### Changed

- Renamed project scripts that were not meaningful/representative to descriptive names, keeping the standardized lowercase `[a-z0-9_.]` convention:
  - `projects/games/skywar/py_game_full.py` → `skywar_game.py` (docstring references in `scoreboard.py` and `user_interface.py` updated).
  - `projects/robotics/sound_processing/tmp4.py` → `knock_detection.py` (its `mlab.run_func('final_judge.m', ...)` call → `'classify_tile.m'`).
  - `projects/robotics/sound_processing/final_judge.m` → `classify_tile.m` (hollow/solid neural-net classifier).
  - `projects/robotics/sound_processing/final_test_gene.m` → `pca_features.m` (PCA feature extraction; internal call in `classify_tile.m` updated).
  - `projects/robotics/sound_processing/jk.m` → `bridge_passthrough.m` (Python↔MATLAB bridge helper).
  - `projects/robotics/sound_processing/dataprocess.m` → `debug_signal_plot.m` (signal-file debug plot helper).
  - `projects/robotics/sound_processing/pyserialcom1/pyserialcom/pyserialcom.ino` → flattened to `knock_spray_controller/knock_spray_controller.ino` (Arduino sketch folder now matches its descriptive name).
  - `projects/computer_vision/face_point_detector_68/dlib_tut.py` → `face_landmark_detector.py`; `example.py` → `face_detection_demo.py` (import updated).
  - `projects/algorithms/python_basic_algorithms/algorithms.py` → `sorting_algorithms.py`.
- All renames done with `git mv`; every internal reference updated; the non-UTF-8 (GBK) comments in the `.m` files left byte-for-byte intact. All 36 user `.py` files still pass `python -m py_compile`; `eslint .` and `vite build` unchanged and passing.
- `package.json` version aligned to `1.8.0`.

## [1.7.0] - 2026-09-25

### Added

- Concise comments and docstrings across the rest of the user code (comments only — no logic, names, literals or behavior changed):
  - `projects/web/personal_web/django_web/` — module docstrings, `# --- <Section> ---` banners and Django-template `<!-- ... -->` comments; spacing normalized in `settings.py`, `models.py`, `views.py`, `urls.py` and the two `admin`/`apps` modules (gallery `resume.css` got group comments, `url("resume_bg.jpg")` preserved).
  - `projects/trading/` — docstrings + section banners for `automated_trading_robot/` and `us_stock_scanner/` modules; verified AST-identical to originals after edits, all nine files compile.
  - `projects/algorithms/python_basic_algorithms/`, `computer_vision/` and `robotics/jenga_ur_robot/` — docstrings, sort/DFS/SIFT stitch comments; URScript Jenga programs got `#` step comments only (all waypoint poses preserved).
  - `src/` (React app) — light comments in `main.jsx`, `app.jsx`, `navbar.jsx`, `walking_worker.jsx`, `home.jsx`, `gallery.jsx`, `projects.jsx`, `data/projects.js`, `app.css` and `index.css`, plus short notes in `vite.config.js` and `eslint.config.js`.

### Changed

- Restored the four canonical docs to their conventional uppercase names — `AGENTS.md`, `LICENSE`, `README.md` and `CHANGELOG.md` (plus per-project `PROJECTS/trading/automated_trading_robot/LICENSE` and `.../django_web/personal_web/static/README.md`), and updated `AGENTS.md`'s own references accordingly.
- Kept the uncommitted `index.html` switch of the favicon/entry paths to relative ones (`public/favicon.svg`, `src/main.jsx`) as requested.
- `package.json` version aligned to `1.7.0`.

## [1.6.0] - 2026-09-24

### Added

- Concise section banners and inline comments across the SkyWar game source and the sound-processing research code (comments only — no logic, names, literals or asset paths changed):

  - `projects/games/skywar/{py_game_full.py, user_interface.py, scoreboard.py}` and `projects/games/skywar/tools/game_score_board.py`: module docstrings, `# --- <Section> ---` banners, sprite/loop/method comments, Python-style blank line discipline.
  - `projects/robotics/sound_processing/{dataprocess.m, jk.m, final_test_gene.m, final_judge.m}`: `%` headers and stepping comments (MATLAB weight matrices and PCA `basis1`/`basis2` left byte-for-byte untouched).
  - `projects/robotics/sound_processing/tmp4.py`: docstrings, serial/MATLAB/PyAudio section comments, removed a stale commented-out tkinter block.
  - `projects/robotics/sound_processing/pyserialcom1/pyserialcom/pyserialcom.ino`: normalized to 2-space indentation with `//` comments (pins, `freq = 20`, delays and Serial strings preserved).
- Normalized line endings (CRLF everywhere except the LF `tools/game_score_board.py`) and verified every `.py` file compiles with `python -m py_compile`.

## [1.5.0] - 2026-09-24

### Changed

- Renamed every tracked file and directory to lowercase `[a-z0-9_.]` (hyphens are excluded because `-` breaks Python `import`). Slugs became underscore-case (`automated-trading-robot` → `automated_trading_robot`, `computer-vision` → `computer_vision`), app files lowercased (`App.jsx` → `app.jsx`, `src/pages/Home.jsx` → `src/pages/home.jsx`), and assets fixed (`UR_jenga.gif` → `ur_jenga.gif`, `MainMenu.PNG` → `main_menu.png`, `Colourful.jpg` → `colourful.jpg`, `clear-blue-sky.jpg` → `clear_blue_sky.jpg`). Excluded: vendored M5Stack library, iCloud stubs (`.FFbgMusic.mp3.icloud`, `.Flying_me_softly.mp3.icloud`) and npm-managed `package-lock.json`.
- Updated every cross-reference: imports in `src/main.jsx`, `src/app.jsx`, `src/pages/home.jsx`; media paths and run commands in `src/data/projects.js` (`stock_APP.py` → `stock_app.py`, `stock_GUI.py` → `stock_gui.py`); README toctree links, images and run instructions; `agents.md` repo map and workflow names (`auto_merge.yml`); and in-repo asset paths in the SkyWar game (`Resources/` → `resources/`, `BadCloud.png` → `bad_cloud.png`, `Bullet.png` → `bullet.png`).
- `package.json` version aligned to `1.5.0` (was `1.2.0`) to match `CHANGELOG.md`.

## [1.4.0] - 2026-09-24

### Changed

- Copy-polished resume wording in `src/pages/Home.jsx` for clarity and presentation while preserving all facts, dates, employers and project names: rewrote run-on sentences, fixed typos (`Adminstrator` → `Administrator`, `millstones` → `milestones`), normalised abbreviations (`IOT` → `IoT`, `SWIFT` → `Swift`, `inno.` → `innovation`), used consistent date ranges (`Oct 2023 – Present`), past-tense duty bullets, and `&lt;strong&gt;` in place of `&lt;b&gt;`.
- Reworded `public/gallery.md` captions and added a page `<meta name="description">` for better SEO/social presentation.

## [1.3.0] - 2026-09-24

### Changed

- Renamed XP state/props from `score`/`addScore` to `xp`/`addXp` across `App.jsx`, `Navbar.jsx` and `Gallery.jsx`, matching the on-screen "XP to Know Me" concept (CSS classes `nav-score`/`score-*` → `nav-xp`/`xp-*`).
- Renamed vague loop and data variables to be self-describing: `Projects.jsx` now uses `category`/`project`/`categoryProjects` instead of `cat`/`p`/`items`, `asset` helper → `assetUrl`; `Gallery.jsx` uses `rawBlocks`/`parsedSections`/`section`/`index`; `Navbar.jsx` uses `navLinks`/`index`/`xpPop`.
- Renamed the ambiguous `run` field in `src/data/projects.js` to `runCommand`.

## [1.2.0] - 2026-09-24

### Changed

- Standardized quoting and formatting across `vite.config.js`, `eslint.config.js` and `package.json`; `package.json` version bumped to `1.2.0`.
- Normalized `rgba(...)` spacing in `src/App.css` and JSX formatting in `Navbar.jsx`, `Projects.jsx` and `Home.jsx`.

### Removed

- Unused `public/icons.svg` sprite and the unused `path` field from all `src/data/projects.js` entries (dead data — the site never reads it).

## [1.1.0] - 2026-09-24

### Added

- `.github/workflows/deploy-reactjs-page.yml` deploys the Vite build to GitHub Pages via the official Pages actions (`upload-pages-artifact` + `deploy-pages`) on every push to `main`, completing the `local → dev-001 → dev → main → deploy` pipeline.

## [1.0.0] - 2026-09-24

### Added

- `/projects` site page (`src/pages/Projects.jsx`) rendering all portfolio entries as cards grouped by category, with role tags, tech chips, run commands and showcase media.
- `src/data/projects.js` as the single source of truth for the portfolio content.
- Root `README.md` rewritten as the toctree: categories → project links, images and run instructions (replaces the deploy-only README).
- `public/projects/<slug>/` showcase media library (18 screenshots/GIFs/videos relocated from project folders).
- Category layout under `projects/` (trading, robotics, computer-vision, embedded-iot, web, games, algorithms).
- `.gitignore` entries for Python venvs, `__pycache__`, `*.pyc`, `.DS_Store`, `db.sqlite3` and `build/`.
- Navbar "Projects" link (60 XP) and route wired in `App.jsx`.
- ESLint toolchain (`eslint`, `@eslint/js`, `globals`, `eslint-plugin-react-hooks@4`, `eslint-plugin-react`, `eslint-plugin-react-refresh`) and repo-local `.npmrc` (`legacy-peer-deps=true`) so `npm run lint` actually runs.

### Changed

- Project folders renamed to kebab-case and grouped by domain (e.g. `Automated_Trading_Robot` → `projects/trading/automated-trading-robot`).
- `AGENTS.md` `projects/` and Gallery sections rewritten for the new layout.
- `eslint.config.js` reworked to attach `react-hooks` rules manually and enable `react/jsx-uses-vars` (fixes JSX false-positives with ESLint 9).
- `public/gallery.md` image URLs switched from absolute `/img/...` to relative `img/...` so they resolve under the `/blog/` subpath.
- `package.json` version bumped to `1.0.0`.

### Removed

- Nested `.git/` directories from all 12 project folders (history remains on their GitHub remotes).
- Per-project `README.md` files (content folded into the toctree and `src/data/projects.js`).
- `Personal_web/django_env/` Python venv (48.7 MB) and `Automated_Trading_Robot/Automated_Bot/` build artifacts (22.2 MB).
- Bytecode caches (1543 `.pyc`, 274 `__pycache__`), `.DS_Store` files, Django `db.sqlite3`, demo uploads, stale `src/assets/` duplicates and unused `Capture.PNG`.
- Empty `Comment-and-Response-Management` placeholder (no source, no commits).

## [0.1.0] - 2026-09-24

### Added

- `AGENTS.md` workflow requirement: every change must update `CHANGELOG.md` (version bump + dated entry) and land as a Git commit with a clear subject and body.
- `CHANGELOG.md` itself, to track versions.
- `AGENTS.md` note on the git flow: work is committed to `dev-001`, which is auto-merged to `dev` then `main` by `.github/workflows/auto-merge.yml`.