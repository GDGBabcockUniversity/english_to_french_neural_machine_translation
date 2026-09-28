# Dataset Guide

How to build a dataset that passes review. Read this before you start collecting.

This guide covers sourcing, cleaning, and splitting. It does not cover the row schema, upload mechanics, or registry rules — those live in the files linked at the bottom.

## Two kinds of datasets

**Training dataset.** Used to fine-tune an adapter. The model learns from these rows. You submit these.

**Test dataset.** Held out. Never trained on. Used to score models with COMET. Almost always built by a maintainer, not a contributor. See [MODELS.md](../MODELS.md) → "What is the held-out test set?"

The rest of this guide is about training datasets unless stated otherwise.

## Where to get data

Real sources that work for English→French:

- **OPUS** — https://opus.nlpl.eu — the largest open collection of parallel corpora. Start here.
- **Tatoeba** — https://tatoeba.org — short sentences, human-translated, CC-BY.
- **WikiMatrix** — Wikipedia article pairs, auto-aligned, good for long sentences.
- **OpenSubtitles** — conversational French, different register from news.
- **Public domain books** with side-by-side translations.

You do not need to build a dataset from scratch. Most good submissions are cleaned, filtered, and deduplicated slices of an existing corpus.

**Before you touch anything, check the license.** If the license forbids redistribution, you cannot put the dataset on the Hugging Face Hub. Record the source URL and license in the HF repo's `README.md`. A submission without a license line is rejected.

**Do not use:**
- Scraped data from sites whose terms of service forbid it.
- Machine-translated data, unless a maintainer has explicitly approved it for a specific submission. Say so in the PR.
- Data whose license you cannot identify.

## The schema

Every row follows the same shape. Read [data/schema.md](../data/schema.md) for the exact JSON. Do not invent keys. Do not rename keys. Do not add metadata fields.

The dataset must be a Hugging Face `datasets`-loadable format. Parquet and JSONL both work.

## Cleaning rules

Every submission must satisfy all of these. A maintainer will spot-check.

- **No duplicate rows.** Deduplicate on the English side.
- **No empty strings.** Both `eng_Latn` and `fra_Latn` must be non-empty after stripping whitespace.
- **No identical pairs.** If `eng_Latn` equals `fra_Latn`, the row is broken.
- **No HTML, no markup, no URLs.** Strip them.
- **No obviously wrong language.** A row where `fra_Latn` is actually English is a bug.
- **No sentence over 512 tokens.** NLLB truncates at 512; longer rows train on partial sentences and produce garbage.
- **Consistent punctuation.** Do not mix French guillemets and English quotes in the same dataset without reason.
- **Stable IDs.** `id` is a unique string within the dataset. Use a monotonic integer as a string, or a hash. Never reuse.

If you cannot enforce one of these programmatically, say so in the PR. Do not silently ship a dataset with known defects.

## Splitting

Training datasets do not need a train/test split. The project's canonical test set is fixed and lives separately — [see MODELS.md](../MODELS.md).

Do not carve a test set out of your training data. It would be too small to score meaningfully, and it would not be comparable to the project's canonical test set.

## Upload to the Hugging Face Hub

Full upload mechanics — CLI install, authentication, repo creation — are in [docs/hf-workflow.md](hf-workflow.md). Read that first.

1. Create the dataset repo under `GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder <dataset-name>`.
2. Upload the parquet or JSONL file.
3. Write a `README.md` inside the HF repo containing:
   - **Exact source URL.** The URL you downloaded from, not the site name. `https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/moses/en-fr.txt.zip` is a source. "OPUS" is not.
   - **Exact download command**, if you used a CLI or script. Copy-pasteable.
   - License, with a link to the license page.
   - Row count.
   - Language pair.
   - Any filtering or cleaning applied.
4. Confirm the Hugging Face dataset viewer can load it without errors.

A submission without an exact URL and a license link is rejected at review. A maintainer must be able to open the source and see the same data.

## Submit the PR

Open a PR against `GDGBabcockUniversity/english_to_french_neural_machine_translation` containing:

- Hugging Face dataset repo ID
- Row count
- License, with a link to the license page
- **Exact source URL** and, if applicable, the exact download command
- The cleaning applied

A maintainer will open your source URL and spot-check rows against it. If the URL does not resolve, or the rows are not found in the source, the PR is rejected.

**Do not edit `DATASETS.md`.** A maintainer adds the registry row at merge time. Do not add a status column. If your dataset is rejected, no row is added — the closed PR is the record.

Review tier: **Low**. CI must be green and one maintainer must approve.

## What gets rejected

- Missing license or unverifiable source.
- Source URL missing, dead, or pointing at a site name instead of a specific file.
- Rows with wrong schema — extra keys, renamed keys, nulls.
- Over 10% of rows failing the cleaning rules.
- Duplicate submissions of a dataset already in the registry.
- Machine-translated data without approval.
- Row count claimed in the PR does not match the HF repo.

## Done when

Your PR is done when the HF repo loads without errors, the row count in the PR matches the HF repo, the license is recorded in the HF `README.md`, and CI is green.

## Related Documentation

- [data/schema.md](../data/schema.md) — exact row shape
- [docs/interfaces.md](interfaces.md) — the contract this schema is part of
- [docs/hf-workflow.md](hf-workflow.md) — how to upload to the Hugging Face Hub
- [DATASETS.md](../DATASETS.md) — the registry and the 20-dataset phase gate
- [MODELS.md](../MODELS.md) — what a test set is and how COMET uses it
- [CONTRIBUTING.md](../CONTRIBUTING.md) — PR flow and review tiers
- [NLLB-200 documentation](https://huggingface.co/docs/transformers/model_doc/nllb)
