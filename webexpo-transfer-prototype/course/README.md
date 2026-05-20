# Full student prototype: AI for student projects

## Course purpose

This mini-course teaches students how to use AI tools on a real-world dataset without pretending that AI output is automatically correct.

The course is designed for the UCT Prague Technology Skills for Project Managers class. It is suitable for students from project management, chemistry, economics, design, IT, bioinformatics, business, and other backgrounds.

A student with no coding background can complete the required course.

The main learning outcome is a reusable workflow:

> project question -> data/context -> AI-assisted analysis -> validation -> decision brief

## What students will build

Students will produce a short AI-supported decision brief from a real-world food-products dataset.

The brief answers:

> Based on available nutrition fields, which product category looks healthier or less healthy, and how confident can we be given missing or inconsistent data?

The point is not nutritional advice. The point is learning how to handle messy real data, use AI carefully, validate output, and explain uncertainty to a project team.

## Dataset

The prototype uses an Open Food Facts-style food-products sample. Open Food Facts is a free, public, crowdsourced food-products database that stores product names, brands, categories, countries, ingredients, allergens/additives, and nutritional information. It is suitable for this class because the data are understandable, interdisciplinary, and messy enough to show real validation problems.

For the classroom prototype, use the included small CSV sample in `../data/sample_food_products.csv`. It is intentionally small enough to inspect manually.

When preparing the final live version, refresh the sample from Open Food Facts and keep only non-sensitive public product-level fields.

## Required versus optional tools

### Required for everyone

- Spreadsheet app: Excel, Google Sheets, or LibreOffice Calc.
- One AI chat assistant: ChatGPT, Gemini, Claude, or a similar tool available to the student.
- Provided CSV file: `../data/sample_food_products.csv`.

### Optional tools

- NotebookLM for source-grounded Q&A over uploaded course files.
- Perplexity or browser search for quick sourced orientation.

### Optional technical tools

- Python 3 and pandas.
- VS Code or another editor.
- Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code.

These technical tools are not required for the main course.

## Student paths

### Path A: beginner no-code path

Recommended for all students and required as the baseline.

Students inspect the CSV in a spreadsheet, use one AI chat tool to structure the analysis, validate the output manually, and write a decision brief.

Students do not need GitHub or programming tools.

### Path B: source-grounded path

Recommended for students who want the AI assistant to answer from a controlled set of uploaded files.

Students can upload course notes, dataset notes, and their own draft brief to NotebookLM or a similar tool.

### Path C: optional technical path

Recommended only for students who already code or want to try.

Students use Python and a coding assistant to explain, run, or improve the small analysis script.

The technical path is not required for completing the course.

## Course structure

1. `01_orientation.md` - what students are doing and why.
2. `02_tool_setup.md` - which tools to use and what to avoid.
3. `03_dataset_walkthrough.md` - how to inspect the data.
4. `04_ai_workflow_no_code.md` - no-code AI workflow.
5. `05_validation_checklist.md` - how to check AI output.
6. `06_decision_brief.md` - final output template.
7. `07_optional_coding_track.md` - optional Python and AI coding assistant path.
8. `08_teacher_notes.md` - lecturer-facing rationale and assessment.

## Final student output

Each student or small group submits:

1. A one-page decision brief.
2. A short AI-use log: which tool was used, what was asked, what was checked manually.
3. A validation checklist with at least three limitations or risks.

## Important rule

AI is allowed as a learning assistant in this prototype, but the student must be able to explain the final result in their own words. The student must not submit AI text without review, validation, and editing.
