# 06 - Final decision brief

## Goal of this module

Turn your AI-assisted analysis into a short project decision brief that a mixed team can understand.

A decision brief is not a long report. It is a concise document that helps a team decide what to do next.

## Required structure

Use this structure.

```text
Title:

1. Objective
What question are we trying to answer?

2. Data used
What dataset, columns, and sample size did we use?

3. Method
What did we inspect manually? What did AI help with?

4. Findings
What patterns were visible in the data?

5. Limitations
What makes the conclusion uncertain?

6. Recommendation
What should the team do next?

7. AI-use log
Which tool did we use, what did we ask, and what did we manually check?
```

## Example brief skeleton

Do not copy this as your final answer. Fill it in with your own checks.

```text
Title: First screening of nutrition patterns in a small food-products sample

1. Objective
The goal was to identify visible nutrition patterns in a small public sample of food products and decide what would need to be checked before using the data in a real project.

2. Data used
I used the provided CSV sample with product names, categories, countries, Nutri-Score grades, energy, sugar, salt, saturated fat, protein, and ingredients text.

3. Method
I first inspected the spreadsheet manually. Then I used [tool name] to help list possible patterns and data-quality risks. I checked the AI output against the spreadsheet before using it.

4. Findings
In this sample, [category] appeared to have higher [field] than [comparison category]. [Another pattern].

5. Limitations
The sample is small. Categories are mixed. Some product types are not directly comparable. The dataset cannot support medical advice.

6. Recommendation
For a real project, the team should [next action], for example collect a larger category-specific sample or define clearer nutrition criteria before making a recommendation.

7. AI-use log
Tool used: [tool].
Prompt used: [short summary].
Manual checks: [what you checked].
Changed after validation: [what you corrected].
```

## Writing rules

Use cautious language.

Prefer:

- "In this sample..."
- "The data suggests..."
- "This would need verification..."
- "The next step should be..."

Avoid:

- "This proves..."
- "AI found the truth..."
- "This food is healthy/unhealthy" without criteria;
- any claim that you cannot point to in the data.

## Final self-check

Before submitting, answer:

1. Can I explain the result without reading AI text?
2. Did I manually verify the main claim?
3. Did I mention limitations?
4. Did I describe how AI was used?
5. Would a non-technical teammate understand the decision?

## Mini-output

At the end of this module, you should have the final one-page brief.
