# 05 - Validation checklist

## Goal of this module

Learn how to check AI-assisted analysis before using it in a project decision.

AI can help organize information, but it can also sound confident when it is wrong, incomplete, or unsupported.

## The validation rule

Before you use an AI answer, check four things:

```text
1. Data: does the answer match the data?
2. Logic: does the reasoning make sense?
3. Scope: is the conclusion too broad?
4. Decision: is the output useful for the actual project question?
```

## Checklist A: data validation

Use the spreadsheet to check:

- Are the numbers mentioned by AI actually present in the data?
- Did AI invent values, products, categories, or averages?
- Are missing values clearly mentioned?
- Are units clear, for example per 100 g or per 100 ml?
- Are product categories consistent enough to compare?
- Are there extreme values that should be checked?

## Checklist B: reasoning validation

Ask:

- Is AI comparing similar products or mixing unrelated categories?
- Did AI confuse a single example with a general trend?
- Did AI confuse correlation with causation?
- Did AI make health claims that the dataset cannot support?
- Did AI ignore sample size?
- Did AI explain uncertainty?

## Checklist C: project-management validation

Ask:

- What decision is this analysis supposed to support?
- Would a non-technical teammate understand the conclusion?
- What would a manager, scientist, designer, or business student need to know before acting?
- What is the next action after this analysis?
- What additional data would be needed for a real decision?

## Red flags in AI output

Be careful when AI says:

- "clearly proves";
- "definitely";
- "the healthiest";
- "the worst";
- "always";
- "never";
- exact averages that you did not calculate;
- claims about health effects that are not in the dataset.

## Safer language

Use cautious project language:

- "In this sample..."
- "Based on available fields..."
- "A possible pattern is..."
- "This requires verification because..."
- "The dataset does not prove..."
- "Before making a real decision, the team would need..."

## Student task

Take one AI-generated answer from Module 04 and mark each sentence as one of:

| Label | Meaning |
|---|---|
| Supported | Directly supported by the data |
| Plausible but not proven | Could be true, but needs more evidence |
| Unsupported | Not shown by the data |
| Too broad | Goes beyond the sample |
| Needs rewrite | Could be correct but wording is too strong |

## Mini-output

At the end of this module, you should have:

1. A corrected version of the AI answer.
2. At least three limitations.
3. At least two checks you performed manually.
