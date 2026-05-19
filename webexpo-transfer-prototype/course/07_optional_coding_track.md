# 07 - Optional coding track

## Goal of this module

Use a small Python script and an AI coding assistant to inspect the same dataset more systematically.

This module is optional. You can complete the course without coding.

## Who should use this path

Use this path if you:

- know basic Python;
- want to learn pandas;
- want to test Codex, Gemini Code Assist, GitHub Copilot, Cursor, or Claude Code;
- want to see how AI can help document and improve a small analysis script.

## Setup

Install Python 3 and pandas.

One possible command:

```bash
pip install pandas
```

Then run:

```bash
python webexpo-transfer-prototype/technical_demo/analyze_food_products.py
```

## What the script does

The script:

1. loads `data/sample_food_products.csv`;
2. checks row and column counts;
3. calculates missing-value counts;
4. groups products into broad categories;
5. summarizes sugar, salt, saturated fat, protein, and energy;
6. writes a summary table to `technical_demo/output/category_summary.csv`.

## How to use an AI coding assistant

Do not ask:

```text
Make this perfect.
```

Ask specific review questions:

```text
Review this script for a beginner audience.
Suggest improvements for readability, missing-value handling, reproducibility, and comments.
Do not add unnecessary complexity.
```

Or:

```text
Explain this script line by line to a student who knows basic Python but has not used pandas much.
```

Or:

```text
Suggest 3 simple sanity checks that would help verify the output table.
```

## Human validation still matters

Even if the script runs, check:

- Did it read the correct file?
- Are numeric columns interpreted as numbers?
- Are categories grouped correctly?
- Are averages meaningful for mixed products?
- Are drinks and solid foods mixed together?
- Does the output match visible examples in the spreadsheet?

## Technical mini-output

If you do this path, add to your final brief:

```text
Optional technical check:
I used a Python script to calculate category summaries. I checked [specific output] manually. The script helped with [specific task], but the interpretation still required human review because [limitation].
```

## Suggested tools

| Tool | Best use here | Caution |
|---|---|---|
| Codex in ChatGPT | Reviewing and explaining the script | Still run and check the code yourself |
| Gemini Code Assist | Beginner-friendly code help | Verify generated changes |
| GitHub Copilot Free | Inline suggestions in editor | Limited free quota |
| Cursor | Project-folder coding workflow | More editor-oriented |
| Claude Code | Strong agentic code work | Usually better for paid/advanced users |

## Rule

The coding assistant can help write or improve code, but you are responsible for the analysis and conclusion.
