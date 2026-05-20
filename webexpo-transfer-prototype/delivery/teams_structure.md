# Microsoft Teams delivery structure

Use this plan if the activity is delivered through Microsoft Teams and submitted through Assignments.

The goal is to make the activity easy to access for students who do not use GitHub or programming tools.

## Where to place materials

Recommended Teams Files structure:

```text
Class Materials/
└── AI for student projects - WebExpo transfer activity/
    ├── 00_START_HERE.pdf
    ├── 01_dataset/
    │   └── sample_food_products.csv
    ├── 02_student_instructions/
    ├── 03_handout/
    ├── 04_prompts/
    ├── 05_examples/
    └── 06_optional_technical/
```

Teacher-only notes can be kept outside Class Materials or in a private teacher folder:

```text
Teacher only/
└── AI for student projects - facilitator notes/
    ├── lesson_plan_40min.pdf
    └── teacher_notes.pdf
```

## Announcement post

Suggested Teams announcement:

```text
New optional/assigned activity: AI for student projects - from messy information to reliable decisions.

Start with 00_START_HERE.pdf in the course files.
You do not need GitHub, Python, Codex, Claude Code, Copilot, Cursor, or paid tools.

For the required activity, use:
1. the provided CSV dataset,
2. Excel, Google Sheets, or LibreOffice,
3. one AI chat assistant such as ChatGPT, Gemini, or Claude.

Your goal is to inspect real-world data, use AI carefully, validate the output, and write a short decision brief with an AI-use log.
The optional technical folder is only for students who want to try Python or coding assistants.
```

## Assignment setup

Suggested assignment title:

```text
AI-supported project decision brief
```

Suggested assignment instructions:

```text
Complete the beginner no-code route of the activity "AI for student projects: from messy information to reliable decisions."

Use the provided food-products CSV dataset, a spreadsheet tool, and one AI chat assistant.

Your task is to produce a short decision brief answering:
Based on available nutrition fields, which product category looks healthier or less healthy, and how confident can we be given missing or inconsistent data?

This is not medical advice. Focus on project decision-making, data quality, validation, and cautious communication.

Submit:
1. one-page decision brief,
2. AI-use log,
3. validation checklist with at least three limitations or risks.

Optional: if you complete the technical path, you may also submit the Python output or a short note about how a coding assistant helped you understand or check the script.
```

## Student submissions

Required submission files:

1. Decision brief: DOCX, PDF, or Teams text submission.
2. AI-use log: included in the brief or submitted separately.
3. Validation checklist: included in the brief or submitted separately.

Optional technical submission:

- `category_summary.csv`;
- modified Python script;
- short technical note.

## Suggested grading/checking criteria

| Criterion | Evidence |
|---|---|
| Clear project question | The brief states the question clearly |
| Data inspection | Student refers to columns, rows, or checked examples |
| Responsible AI use | AI-use log says what AI was asked to do |
| Validation | At least one AI claim was checked manually |
| Limitations | At least three limitations or risks are listed |
| Cautious wording | Student avoids unsupported health claims |
| Decision focus | Brief includes recommendation or next action |

## Required versus optional work

Make the distinction explicit in Teams.

Required no-code work:

- open the CSV;
- inspect the data;
- use one AI chat assistant;
- validate output;
- write the brief.

Optional technical work:

- run Python;
- use Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code;
- inspect generated summary CSV.

Students should not lose points for skipping the technical path.

## Recommended files to attach to the assignment

Attach or link:

- `00_START_HERE.pdf`
- `sample_food_products.csv`
- `ai_project_checklist.pdf`
- `prompt_pack.pdf`
- `decision_brief_template.docx` if available
- `example_decision_brief.pdf`

## Feedback note for students

Suggested feedback phrase:

```text
The strongest submissions do not simply copy AI output. They show that you inspected the data, used AI to structure thinking, validated claims manually, and communicated uncertainty clearly.
```
