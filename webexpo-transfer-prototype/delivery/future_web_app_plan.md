# Future web app plan

A web app is not needed for the first version of this activity.

The first version should be delivered through Teams or Google Drive because it is simpler, more reliable, and easier for all students to access.

## Why not build a web app first

A web app could create unnecessary friction:

- students may need another account or link;
- the app may distract from the core learning workflow;
- maintenance becomes extra work;
- the course can already be completed with a spreadsheet and one AI chat assistant;
- the first priority is to test the learning activity, not the interface.

The main learning outcome is not using a custom app. The main outcome is:

> define a question, inspect data, use AI carefully, validate output, and write a decision brief.

## When a web app might become useful

A web app could be useful later if:

- the activity is repeated with more students;
- students struggle to follow the file-based workflow;
- the lecturer wants a guided step-by-step interface;
- the activity becomes a larger course module;
- there is a need to collect structured outputs.

## Possible app name

**AI Project Decision Brief Builder**

## App purpose

The app would guide students through the same workflow already present in the course materials.

It should not replace AI tools or validation. It should help students move through the process in a structured way.

## Possible screens

### 1. Start / choose route

Students choose:

- beginner no-code route;
- source-grounded route;
- optional technical route.

The app reminds students that no coding is required for the main activity.

### 2. Open dataset

Students view the dataset description and download/open the CSV.

Possible features:

- show column names;
- explain what each column means;
- warn about missing values and mixed categories.

### 3. Define question

Students write their project question.

The app can provide examples:

- weak question;
- improved project question;
- final selected question.

### 4. Copy AI prompt

The app shows a prompt template.

Students copy it into ChatGPT, Gemini, Claude, or another AI assistant.

The app should not require a built-in LLM for the first version.

### 5. Paste AI output

Students paste the AI response back into the app.

The app asks:

- which claims are factual;
- which claims are assumptions;
- which claims need manual checking.

### 6. Validation checklist

Students mark:

- checked in spreadsheet;
- unsupported;
- too broad;
- needs cautious wording;
- requires more data.

### 7. Decision brief export

The app helps students produce a structured brief:

- objective;
- data used;
- method;
- findings;
- limitations;
- recommendation;
- AI-use log.

Export options:

- copy to clipboard;
- download Markdown;
- download DOCX or PDF later if implemented.

## Possible prototype tools

### Claude Artifact

Useful for:

- quick interactive checklist;
- simple decision brief builder;
- fast classroom demo.

Limitations:

- access may depend on Claude availability;
- not ideal as the only course delivery method;
- app behavior and sharing may depend on platform constraints.

### Lovable

Useful for:

- a polished no-code prototype;
- building screens quickly;
- demonstrating the idea to a lecturer.

Limitations:

- another platform to maintain;
- may require account setup;
- could distract from the simple course workflow;
- not necessary for the first version.

### Simple static app later

A lightweight static app could be built with HTML, CSS, and JavaScript.

Useful features:

- no login;
- works from GitHub Pages;
- no backend;
- no private data collection;
- students can use it as a guided worksheet.

## Recommendation

Do not build the app before testing the file-based course.

Recommended order:

1. Deliver through Teams or Google Drive.
2. Test with at least one beginner user.
3. Collect friction points.
4. Build a static site if navigation is the problem.
5. Build a small web app only if students need guided interaction.

## Success criteria for a future app

A future app is worth building only if it:

- reduces confusion;
- preserves manual validation;
- does not require paid tools;
- does not require GitHub;
- does not collect sensitive data;
- exports a decision brief students can explain in their own words.
