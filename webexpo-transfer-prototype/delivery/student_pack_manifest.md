# Student pack manifest

This manifest lists the files that should be included in a simple student package for Teams or Google Drive delivery.

## Required student pack

| Source repo path | Student-facing filename | Format | Required? | Purpose |
|---|---|---|---:|---|
| `webexpo-transfer-prototype/START_HERE.md` | `00_START_HERE.pdf` | PDF | Yes | First file students read; explains beginner route and required tools. |
| `webexpo-transfer-prototype/data/sample_food_products.csv` | `01_dataset/sample_food_products.csv` | CSV | Yes | Main dataset for spreadsheet inspection and AI-assisted analysis. |
| `webexpo-transfer-prototype/course/01_orientation.md` | `02_student_instructions/01_orientation.pdf` | PDF | Yes | Explains scenario, learning goal, and final output. |
| `webexpo-transfer-prototype/course/02_tool_setup.md` | `02_student_instructions/02_tool_setup.pdf` | PDF | Yes | Explains required and optional tools. |
| `webexpo-transfer-prototype/course/03_dataset_walkthrough.md` | `02_student_instructions/03_dataset_walkthrough.pdf` | PDF | Yes | Guides students through manual dataset inspection. |
| `webexpo-transfer-prototype/course/04_ai_workflow_no_code.md` | `02_student_instructions/04_ai_workflow_no_code.pdf` | PDF | Yes | Shows how to use AI without coding. |
| `webexpo-transfer-prototype/course/05_validation_checklist.md` | `02_student_instructions/05_validation_checklist.pdf` | PDF | Yes | Teaches students how to check AI output. |
| `webexpo-transfer-prototype/course/06_decision_brief.md` | `02_student_instructions/06_decision_brief_template.docx` | DOCX | Yes | Editable template or instructions for final decision brief. |
| `webexpo-transfer-prototype/handout/ai_project_checklist.md` | `03_handout/ai_project_checklist.pdf` | PDF | Yes | One-page checklist for the activity. |
| `webexpo-transfer-prototype/prompts/prompt_pack.md` | `04_prompts/prompt_pack.pdf` | PDF | Yes | Prompt examples for AI use, validation, and decision brief preparation. |
| `webexpo-transfer-prototype/examples/beginner_walkthrough.md` | `05_examples/beginner_walkthrough.pdf` | PDF | Yes | Example of how a beginner can complete the workflow. |
| `webexpo-transfer-prototype/examples/example_decision_brief.md` | `05_examples/example_decision_brief.pdf` | PDF | Yes | Example final brief with cautious wording and AI-use log. |

## Optional technical pack

| Source repo path | Student-facing filename | Format | Required? | Purpose |
|---|---|---|---:|---|
| `webexpo-transfer-prototype/course/07_optional_coding_track.md` | `06_optional_technical/optional_coding_track.pdf` | PDF | Optional | Explains optional Python/coding-assistant route. |
| `webexpo-transfer-prototype/technical_demo/README.md` | `06_optional_technical/technical_readme.pdf` | PDF | Optional | Explains how to run the technical demo. |
| `webexpo-transfer-prototype/technical_demo/analyze_food_products.py` | `06_optional_technical/analyze_food_products.py` | PY | Optional | Simple Python analysis script. |
| `webexpo-transfer-prototype/technical_demo/output/category_summary.csv` | `06_optional_technical/category_summary.csv` | CSV | Optional | Tested example output from the Python script. |

## Teacher/facilitator pack

| Source repo path | Teacher-facing filename | Format | Required? | Purpose |
|---|---|---|---:|---|
| `webexpo-transfer-prototype/lesson_plan_40min.md` | `07_teacher_notes/lesson_plan_40min.pdf` | PDF | Teacher | Facilitator plan for running the activity live. |
| `webexpo-transfer-prototype/course/08_teacher_notes.md` | `07_teacher_notes/teacher_notes.pdf` | PDF | Teacher | Rationale, assessment criteria, and WebExpo connection. |
| `webexpo-transfer-prototype/delivery/README.md` | `07_teacher_notes/delivery_strategy.pdf` | PDF | Teacher | Explains Drive/Teams delivery and repo role. |
| `webexpo-transfer-prototype/delivery/teams_structure.md` | `07_teacher_notes/teams_structure.pdf` | PDF | Teacher | Teams assignment and announcement plan. |
| `webexpo-transfer-prototype/delivery/google_drive_structure.md` | `07_teacher_notes/google_drive_structure.pdf` | PDF | Teacher | Drive folder plan. |

## Optional ZIP package

A ZIP package can be useful if students download materials once and work offline.

Suggested ZIP name:

```text
AI_for_student_projects_student_pack.zip
```

Include:

- start guide;
- dataset;
- student instructions;
- checklist;
- prompt pack;
- examples;
- optional technical folder.

Do not include teacher-only files in the student ZIP unless the lecturer wants them visible.

## Export notes

Markdown files should be exported to PDF for students unless the class is comfortable reading Markdown.

The decision brief template should be provided as DOCX or Google Doc because students need to edit it.

The CSV should remain CSV.

Python files should remain `.py` in the optional technical folder.
