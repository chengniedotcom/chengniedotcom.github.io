# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic website for Cheng Nie (chengnie.com), built on Jekyll with the Academic Pages theme. Hosted on GitHub Pages.

## Development Commands

```bash
# Serve locally with live reload
bundle exec jekyll serve --trace

# Install dependencies (after cloning or when Gemfile changes)
bundle install
```

## Git Workflow

Commits go directly to `master` branch. GitHub Pages deploys automatically on push.

```bash
git add --all
git commit -m "description"
git push origin master
```

## Content Architecture

### Collections (in `_config.yml`)
- `_posts/` - Blog posts organized by language: `en/` and `cn/` subdirectories
- `_notes/` - Book notes/summaries (mostly Chinese titles as markdown files)
- `_pages/` - Static pages (research.md, notes.md, marathon.html, etc.)
- `_teaching/`, `_publications/`, `_portfolio/`, `_talks/` - Academic content collections

### Key Pages
- `_pages/notes.md` - Book notes grid with Goodreads-style covers
- `_pages/marathon.html` - Marathon race history with embedded map
- `_pages/research.md` - Research papers and projects

### Navigation
Site navigation defined in `_data/navigation.yml`. Currently active: Blog, Notes. Research and Teaching are accessible via the front page but removed from the nav bar.

## Helper Scripts

### `marathon.py`
Updates marathon tracking. Reads from `marathon.tsv` (location, date, time, event format), geocodes locations, generates `marathon/map.html`, and updates `_pages/marathon.html` table.

```bash
python marathon.py
```

### `notes_add_text.py`
Processes Goodreads HTML widget output. Paste HTML into the `html` variable at top of file, then run to update `_pages/notes.md` with formatted book cover grid entries.

```bash
python notes_add_text.py
```

## Content Conventions

### Blog Posts (Chinese translations)
When creating Chinese translations of English posts:
- Place in `_posts/cn/` directory
- Add `-cn` suffix to filename after date (e.g., `2026-01-04-cn-review2025.md`)
- Use metric units (km, Celsius) instead of imperial
- Keep book titles/authors in original language, translate summaries

### Book Notes
- Stored in `_notes/` as markdown files
- Filename is URL slug (e.g., `看见.md` → `/notes/看见`)
- Remove `$` characters to prevent LaTeX interpretation

## Analytics

- **Google Analytics 4** (GA4) via `_includes/analytics-providers/google.html` with measurement ID in `_config.yml`
- **Page view badges** via hits.seeyoufarm.com, embedded in `_layouts/single.html` footer

## File Locations

- Site builds to `_site/` (git-ignored for local, committed on some branches)
- Images in `images/`
- Downloadable files in `files/`
- SCSS styles in `_sass/`

## Project Files

- `CHANGELOG.md` - History of site updates (formerly UPDATES.md)
- `TASKS.md` - Organized task tracker (In Progress / Todo / Done)
- `PROMPTS.md` - Saved prompts for recurring workflows
- `CLAUDE.md` - This file (instructions for Claude)
