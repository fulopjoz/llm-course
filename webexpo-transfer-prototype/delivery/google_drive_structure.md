# Google Drive delivery structure

Use this structure if the course is shared through Google Drive.

The goal is to make the activity easy for students who do not use GitHub or coding tools.

## Recommended folder name

```text
AI for student projects - WebExpo transfer activity
```

## Folder structure

```text
AI for student projects - WebExpo transfer activity/
├── 00_START_HERE.pdf
├── 01_dataset/
│   └── sample_food_products.csv
├── 02_student_instructions/
│   ├── 01_orientation.pdf
│   ├── 02_tool_setup.pdf
│   ├── 03_dataset_walkthrough.pdf
│   ├── 04_ai_workflow_no_code.pdf
│   ├── 05_validation_checklist.pdf
│   └── 06_decision_brief_template.docx
├── 03_handout/
│   └── ai_project_checklist.pdf
├── 04_prompts/
│   └── prompt_pack.pdf
├── 05_examples/
│   ├── beginner_walkthrough.pdf
│   └── example_decision_brief.pdf
├── 06_optional_technical/
│   ├── technical_readme.pdf
│   ├── analyze_food_products.py
│   └── category_summary.csv
└── 07_teacher_notes/
    ├── lesson_plan_40min.pdf
    └── teacher_notes.pdf
```

## Student-facing files

Students should mainly use:

- `00_START_HERE.pdf`
- `01_dataset/sample_food_products.csv`
- `02_student_instructions/`
- `03_handout/ai_project_checklist.pdf`
- `04_prompts/prompt_pack.pdf`
- `05_examples/beginner_walkthrough.pdf`
- `05_examples/example_decision_brief.pdf`

## Teacher-only or teacher-first files

The folder `07_teacher_notes/` is mainly for the lecturer or facilitator.

It can be hidden from the first student release if the teacher wants a cleaner package.

## Format recommendations

| Source material | Google Drive format | Reason |
|---|---|---|
| Start guide | PDF | Easy to open, stable formatting |
| Course modules | PDF | Students can read without Markdown knowledge |
| Decision brief template | DOCX or Google Doc | Students can copy and edit |
| Dataset | CSV | Opens in Excel, Sheets, LibreOffice |
| Checklist | PDF | Handout-style reference |
| Prompt pack | PDF and optional Google Doc | PDF for reading, Google Doc for copying prompts |
| Beginner walkthrough | PDF | Example reference |
| Example decision brief | PDF | Prevents accidental editing |
| Python script | PY | Keep original for optional technical students |
| Technical output | CSV | Can be inspected in spreadsheet |
| Teacher notes | PDF | Stable lecturer reference |

## Editable versus read-only files

Keep these editable or copyable:

- decision brief template;
- prompt pack if shared as Google Doc;
- student submission template if created later.

Keep these read-only:

- start guide;
- instructions;
- checklist;
- examples;
- teacher notes.

Keep the dataset unchanged:

- `sample_food_products.csv` should be distributed as a clean original file.
- If students modify it, they should work on their own copy.

## Suggested sharing settings

For the student folder:

- students can view and download;
- students should not edit original files;
- provide a separate editable template if needed.

For the teacher folder:

- lecturer/facilitator can edit;
- students can view only if appropriate.

## Suggested Drive announcement

```text
Please start with 00_START_HERE.pdf.
You do not need GitHub, Python, or paid AI tools.
For the required activity, use the CSV file, a spreadsheet tool, and one AI chat assistant.
Your final output is a short decision brief and AI-use log.
The optional technical folder is only for students who want to try Python or coding assistants.
```
