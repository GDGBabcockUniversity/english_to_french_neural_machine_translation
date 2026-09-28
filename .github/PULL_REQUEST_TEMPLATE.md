<!-- Title format: <type>: <short description>
Examples:
docs: clarify local setup steps
backend: validate translation input
training: add French evaluation split
-->

## What does this PR do?

<!-- Write one or two sentences describing the change. -->

Closes # 
## Which part of the project?

<!-- Check exactly one. -->

- [ ] datasets
- [ ] training
- [ ] backend
- [ ] frontend
- [ ] docs
- [ ] infra

## Review tier

<!--
- Low — docs, tests, frontend, `.github/**`. CI green + 1 maintainer approval.
- Medium — `training/`, `backend/`. CI green + owner or named maintainer, reviewer reads the diff.
- High — `docs/interfaces.md`, any requirements file, new model, tokenizer change, dependency swap. Owner only. Requires reproducible eval numbers, HF link, training notebook, notebook settings, data reference, registry row.
- Unsure → higher tier. Multiple paths → highest tier applies.
-->

- [ ] Low
- [ ] Medium
- [ ] High


## If this PR changes `training/` or `backend/`

<!-- Skippable. Complete this section only when this PR changes `training/` or `backend/`. -->

- [ ] Confirm the interface contract is unchanged or describe the change below.
- [ ] Confirm `pytest tests/` passed locally.

Interface changes: `None`

## If this PR is a fine-tuned model (base model + fine-tuned adapter) submission

<!-- Skippable. Complete this section only when this PR submits a fine-tuned model (base model + fine-tuned adapter). -->

- [ ] Provide the Hugging Face adapter repo ID.
- [ ] Provide the dataset reference.
- [ ] Include the training notebook and Kaggle notebook URL.
- [ ] Provide COMET numbers for both the fine-tuned model (base model + fine-tuned adapter) and the base model on the same split.

### Numbers

Fine-tuned model (base model + fine-tuned adapter):

Base:

### Paths

<!--
Example:
Adapter repo ID: GDGBabcockUniversity-26/english_to_french_nmt_adapters
Subfolder: submission-001
Training notebook: training/train.ipynb
Kaggle notebook URL: https://www.kaggle.com/code/yourname/submission-001
-->

- Adapter repo ID:
- Training notebook: (example: `training/train.ipynb`)
- Kaggle notebook URL: (the link to the run on Kaggle)

## Done when

<!-- Write one checkable condition that a reviewer can verify without asking.
Example: The new backend validation rejects an empty `text` value with HTTP 400.
-->

- [ ] 

## Doesthis PR submit a dataset?

<!-- Skip this whole section if your answer is no. -->

- [ ] Hugging Face dataset repo ID is provided below.
- [ ] Exact source URL is provided below.
- [ ] License is stated, with a link to the license page.
- [ ] Row count matches the HF dataset viewer.
- [ ] Cleaning applied is described below.

### Dataset

- HF dataset repo ID:
- Exact source URL:
- Download command (if any):
- License:
- License page URL:
- Row count:
- Cleaning applied:

## Where to ask

Read `CONTRIBUTING.md` first, then comment on this PR. Do not open a new issue.