# Static site plan

A static website can make the course easier to browse and present to the lecturer, but it should be added after the file-based version works.

The first delivery should remain Teams or Google Drive.

## Goals of a static site

A static site should:

- make the materials easier to navigate;
- provide a clean lecturer-facing preview;
- keep the no-code beginner route visible;
- link to dataset, checklist, prompt pack, and examples;
- keep optional technical content clearly separated.

It should not require students to create GitHub accounts.

## Option 1: GitHub Pages

GitHub Pages is the simplest route if the repository is already on GitHub.

### Advantages

- no new platform needed;
- easy link sharing;
- works well for static documentation;
- can be updated from the same repo;
- students can read the site without GitHub login.

### Disadvantages

- plain GitHub Pages may look basic without extra setup;
- navigation can be less polished than a documentation framework;
- setup may require repository settings.

### Best use

Use GitHub Pages for a simple public or semi-public read-only site once the course structure is stable.

## Option 2: MkDocs Material

MkDocs Material is a documentation framework that turns Markdown files into a polished website with navigation and search.

### Advantages

- clean course-like layout;
- good navigation;
- search support;
- works well with Markdown;
- can be hosted on GitHub Pages.

### Disadvantages

- requires setup files such as `mkdocs.yml`;
- may require local installation or GitHub Actions;
- slightly more technical than plain GitHub Pages.

### Best use

Use MkDocs Material if the course grows beyond a few files or if the lecturer wants a polished browsing experience.

## Option 3: Google Sites

Google Sites is a no-code website builder.

### Advantages

- easy to edit manually;
- familiar to many non-technical users;
- good for sharing within a school or Google Workspace;
- no coding setup.

### Disadvantages

- content may drift from the GitHub source of truth;
- harder to version control;
- less convenient for technical files such as CSV/Python;
- manual updates can become tedious.

### Best use

Use Google Sites if the lecturer or course team prefers a fully no-code site and does not need tight version control.

## Recommendation

Recommended path:

1. Deliver the first version through Teams or Google Drive.
2. Keep GitHub as the source of truth.
3. If a website is useful, start with GitHub Pages.
4. If navigation becomes important, move to MkDocs Material hosted on GitHub Pages.
5. Use Google Sites only if the course team prefers a no-code website and accepts manual updating.

## Proposed site navigation

```text
Home
Start here
Beginner route
  Orientation
  Tool setup
  Dataset walkthrough
  No-code AI workflow
  Validation checklist
  Decision brief
Student materials
  Dataset
  One-page checklist
  Prompt pack
  Beginner walkthrough
  Example decision brief
Optional technical route
  Coding track
  Python demo
Teacher materials
  40-minute lesson plan
  Teacher notes
Delivery
  Teams delivery
  Google Drive delivery
```

## Minimal GitHub Pages approach

A minimal first version can use the existing Markdown files and a simple `index.md`.

Possible next files:

- `index.md`
- `_config.yml` for GitHub Pages theme

## MkDocs approach

Possible later files:

- `mkdocs.yml`
- `docs/` folder containing copied or reorganized Markdown files
- GitHub Actions workflow for deployment

This should be treated as a later polish step, not a prerequisite for teaching the activity.
