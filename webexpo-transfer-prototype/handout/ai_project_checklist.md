# One-page checklist: AI-supported student project

Use this checklist during the activity.

## 1. Define the question

Before using AI, write one clear project question.

Good question:

```text
In this small sample, which product categories show higher sugar, salt, or saturated-fat values, and what limitations should we mention before making a project recommendation?
```

Avoid vague questions such as:

```text
Which food is healthy?
```

## 2. Inspect the data yourself

Open `data/sample_food_products.csv` in a spreadsheet.

Check:

- How many rows are there?
- What columns are available?
- Which categories appear?
- Are any values missing?
- Are product types mixed, for example drinks, spreads, snacks, dairy, sauces?
- Are units clear, for example values per 100 g or 100 ml?

## 3. Ask AI safely

Use this prompt pattern:

```text
Context: I am a student using a small public food-products dataset.
Task: Help me identify visible patterns and data-quality risks.
Constraints: Do not invent values. Separate facts from assumptions. Do not make medical claims.
Output: Give me a short list of patterns and a validation checklist.
```

## 4. Validate AI output

For each important AI claim, ask:

- Can I see this in the spreadsheet?
- Did AI invent a number, average, product, or category?
- Is the comparison fair?
- Is the sample too small for the claim?
- Is the wording too strong?
- Does the claim answer the project question?

## 5. Use cautious language

Prefer:

- "In this sample..."
- "The data suggests..."
- "A possible pattern is..."
- "This requires verification..."
- "The dataset does not prove..."

Avoid:

- "This proves..."
- "Definitely..."
- "Always..."
- "The healthiest..."
- "The worst..."

## 6. Write the decision brief

Use this structure:

```text
Title:
Objective:
Data used:
Method:
Findings:
Limitations:
Recommendation:
AI-use log:
```

## 7. Record AI use

Write:

- which AI tool you used;
- what you asked it to do;
- what you checked manually;
- what you changed after validation;
- what limitations remain.

## 8. Final self-check

Before submitting or presenting, answer:

- Can I explain the result without reading AI text?
- Did I verify the main claim manually?
- Did I mention limitations?
- Did I avoid private or sensitive data?
- Would a non-technical teammate understand the recommendation?
