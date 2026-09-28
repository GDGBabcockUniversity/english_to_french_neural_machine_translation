# Contributing

## Table of Contents
- [1. Welcome](#1-welcome)
- [2. Code of Conduct](#2-code-of-conduct)
- [3. Ways to contribute](#3-ways-to-contribute)
- [4. Prerequisites](#4-prerequisites)
- [5. Contribution flow](#5-contribution-flow)
- [6. The interface contract](#6-the-interface-contract)
- [7. Hugging Face Hub policy](#7-hugging-face-hub-policy)
- [8. Registry tables](#8-registry-tables)
- [9. Phase gate](#9-phase-gate)
- [10. Review tiers](#10-review-tiers)
- [11. Acceptance rubric](#11-acceptance-rubric)
- [12. What gets rejected](#12-what-gets-rejected)
- [13. What good looks like](#13-what-good-looks-like)
- [14. Where to ask](#14-where-to-ask)
- [15. CI, in one paragraph](#15-ci-in-one-paragraph)

---

## 1. Welcome

Beginners are welcome here. This is a university club Hacktoberfest project, and you do not need prior open-source experience to contribute. Your first PR is usually small: fixing a test, clarifying a document, correcting a frontend issue, or making another focused change is enough.

---

## 2. Code of Conduct

Participation in this project means agreeing to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 3. Ways to contribute

### Labels

Issues carry two labels.

**Difficulty** — pick based on how much context you need:

- **`good first issue`** — small, self-contained, no project context needed. Start here.
- **`help wanted`** — larger, or requires reading part of the codebase first.

**Topic** — what part of the project the issue touches:

`datasets`, `training`, `backend`, `frontend`, `docs`, `infra`

Every issue has one difficulty label and one topic label. Filter the Issues tab by both to find something that fits you. Example filter: `good first issue` + `frontend` shows only frontend tasks suitable for a first PR.

To claim an issue, comment on it.

### Streams

Each stream below states: what you do, what file you touch, and how you know you are done.

**Datasets** — `help wanted`. Not a first PR.
Collect or clean an English–French corpus, push it to Hugging Face Hub as `YOUR-CLUB/<name>`, and open a PR linking the HF repo.
Touch: the new HF repo. Do not edit `DATASETS.md` — a maintainer adds the row at merge.
Done when: CI's schema check against the HF dataset passes.
Requires: a Hugging Face account, and `docs/dataset-guide.md`.

**Training** — `help wanted`. Not a first PR.
Open `training/train.ipynb` on Kaggle (or locally if you have a GPU), edit the settings cell, and run all cells.
Touch: `training/train.ipynb` (settings only).
Done when: the notebook runs to completion and saves an adapter to `./models/`.

**Evaluation** — `good first issue`. Good first PR.
Add one test case to `tests/test_eval.py` — an input the current evaluation notebook mishandles.
Touch: `tests/test_eval.py`.
Done when: `pytest tests/test_eval.py` passes.

**Backend** — `good first issue`. Good first PR.
Add one test to `tests/test_api.py`. Example: POST `/translate` with `{"text": ""}` and assert the response is 400.
Touch: `tests/test_api.py`.
Done when: `pytest tests/test_api.py` passes.

**Frontend** — `good first issue`. Good first PR.
Pick an open issue labeled `frontend` and fix it under `frontend/`. Example: the output box overflows on narrow screens.
Touch: files under `frontend/`.
Done when: the page works at the widths listed in the issue.

**Docs** — `good first issue`. Good first PR.
Fix a broken link, a typo, or a step in `docs/` that did not work when you followed it.
Touch: one file under `docs/`.
Done when: the doc reads correctly end to end and the change is small.

**Infra** — `help wanted`. Not a first PR.
Propose one specific change to `.github/workflows/ci.yml`, for example cache pip dependencies to cut CI time.
Touch: `.github/workflows/ci.yml`.
Done when: CI is faster on your PR and all existing checks still pass.

---

## 4. Prerequisites

You need:

- [git](https://git-scm.com/downloads)
- Python 3.10 or newer
- A GitHub account

A Hugging Face account is required only if you are contributing a dataset or a fine-tuned model.

See [docs/setup.md](docs/setup.md) for the project setup instructions.

---

## 5. Contribution flow

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone <your-fork-url>
   cd english_to_french_neural_machine_translation
   ```
3. Create a branch. Use the prefix that matches your change:
   - `feat/<short-name>` — new behavior
   - `fix/<short-name>` — broken behavior corrected
   - `docs/<short-name>` — text only, no code behavior change

   Example: `git checkout -b fix/empty-text-400`
4. Make the change. Keep the PR scoped to one thing.
5. Run the tests locally:
   ```bash
   pytest
   ```
6. Commit using the prefix that matches your change:
   - `feat:` — new behavior
   - `fix:` — broken behavior corrected
   - `docs:` — text only
   - `test:` — tests only
   - `chore:` — tooling, configs, dependencies

   Example: `git commit -m "test: add empty text API case"`
7. Push the branch to your fork:
   ```bash
   git push origin <your-branch-name>
   ```
8. Open a pull request against `main`. Fill the PR template fully.
9. Respond to review comments. Do not force-push after review has started unless asked.

---

## 6. The interface contract

`docs/interfaces.md` is the source of truth.

- **Data row:** Each dataset row is `{"id": str, "translation": {"eng_Latn": str, "fra_Latn": str}}`. No extra keys, no renamed keys, no null values.
- **Training:** Training is run by opening `training/train.ipynb` and running all cells. It saves the adapter to `./models/`.
- **API:** `POST /translate` with body `{"text": "hello"}` returns `{"translation": "bonjour"}`. Missing or empty text returns 400. Model failure returns 500. No other fields.
- **Model:** Must be a seq2seq model loadable via `AutoModelForSeq2SeqLM.from_pretrained(...)` with an NLLB tokenizer. No classification heads, no custom architectures.

CI enforces these. If a test fails because an interface changed, the PR does not merge.

---

## 7. Hugging Face Hub policy

Datasets and models live on the Hugging Face Hub, never in git.

Each dataset gets its own Hugging Face repository. Each model gets its own Hugging Face repository. Contributions reference these repositories by ID, such as `YOUR-CLUB/<name>`, never by a local file path.

A PR adding a dataset or model must include:

- Hugging Face repository ID
- Training notebook
- Notebook settings
- Evaluation notebook
- COMET score against the held-out test set

A model without reproduction is rejected. Do not edit `DATASETS.md` or `MODELS.md` — a maintainer adds the row at merge.

---

## 8. Registry tables

`DATASETS.md` and `MODELS.md` are the project registries. They record approved datasets and models so contributors can see what has been accepted without searching through individual pull requests.

Contributors do not edit these files. A maintainer adds one row at merge time, after the PR passes CI and review. The PR label `approved` marks the merge.

### `DATASETS.md` row format

| Name | Hugging Face repo ID | Contributor | Rows | Language pair | Date approved |
| --- | --- | --- | --- | --- | --- |
| en-fr-train-001 | GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder train-001 | @your-github-handle | 50000 | eng_Latn / fra_Latn | 2025-10-01 |

### `MODELS.md` row format

| Name | Hugging Face repo ID | Base model | Contributor | COMET | Dataset | Date approved |
| --- | --- | --- | --- | --- | --- | --- |
| submission-001 | GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder submission-001 | facebook/nllb-200-distilled-1.3B | @your-github-handle | 0.87 | en-fr-train-001 | 2025-10-01 |

The rows above are examples showing the format. They are not real entries.

---

## 9. Phase gate

Dataset collection is capped at **20 approved repositories**.

Once 20 rows exist in `DATASETS.md`, dataset collection closes and no new dataset PRs are accepted.

This is a phase gate, not a temporary review delay. It exists so the project can move from collecting data to training on it.

---

## 10. Review tiers

### Part A — Why the tiers exist

A single review policy collapses to one of two failure modes: the owner reviews everything and becomes the bottleneck, or nothing is reviewed and quality becomes meaningless. Tiers map risk to required scrutiny. The amount of review is proportional to the damage a bad merge causes. A typo fix and a new model do not deserve the same gate.

### Part B — Review tier requirements

| Tier | What it covers | Damage if merged badly | Who approves | Evidence required before merge |
| --- | --- | --- | --- | --- |
| **Low** | Docs, tests, frontend, issue/PR templates | A confusing doc, a broken page, a flaky test. Reversible in one commit. No downstream breakage. | Any maintainer. One approval. | CI green. |
| **Medium** | Training loop, backend logic, data loader, eval script | Silently degrades model quality, or breaks `/translate` for every frontend user. CI passes because the code runs, just runs wrong. | Owner or a named maintainer. One approval. Reviewer must read the diff. | CI green. Tests covering the change. |
| **High** | New model, tokenizer change, dependency swap, interface change | Pollutes the registry, invalidates prior eval comparisons, or breaks every downstream consumer at once. Not reversible by a single revert if the HF ID is already referenced. | Owner only. | CI green. Reproducible COMET numbers. HF Hub link. Training notebook. Notebook settings. Data reference. |

### Part C — Path lookup

| Path | Tier |
| --- | --- |
| `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE` | Low |
| `.github/**` | Low |
| `docs/**` | Low |
| `frontend/**` | Low |
| `tests/**` | Low |
| `data/schema.md` | Low |
| `training/train.ipynb` | Medium |
| `training/eval.ipynb` | Medium |
| `backend/**` | Medium |
| `docs/interfaces.md` | High |
| `requirements.txt`, `training/requirements.txt`, `backend/requirements.txt` | High |
| Adding a model referenced in `MODELS.md` | High |
| Changing tokenizer, base model, or language codes | High |

If you are unsure which tier a PR falls into, treat it as the higher tier. If a PR touches multiple paths, the highest tier among them applies. Tables A and B are the reviewer contract.

---

## 11. Acceptance rubric

A PR merges when:

1. CI passes.
2. Interfaces are respected.
3. For model PRs: COMET improves or holds on the held-out test set. For non-model PRs: CI green and interfaces respected.
4. A maintainer approves according to the review tier.

Rejections are mechanical and predictable, not personal. If a PR fails any of 1–4, it is closed with the failing criterion named.

---

## 12. What gets rejected

The following contributions are rejected:

- Large binaries in git.
- Model blobs without reproduction.
- Interface violations.
- Logic changes without tests.
- PRs that skip the PR template.
- PRs that bundle unrelated changes.

---

## 13. What good looks like

### Example 1 — Documentation

**Bad:**

```text
Prepare dataset with NLLB-200 requirements.
```

**Good:**

```json
{
  "id": "1",
  "translation": {
    "eng_Latn": "I am a boy",
    "fra_Latn": "je suis un garçon"
  }
}
```

The documentation must also link to the NLLB-200 documentation on Hugging Face so contributors can verify the language-code format.

### Example 2 — PR description

**Bad:**

```text
Fixed stuff.
```

**Good:**

```text
CI status: Green

Interfaces respected: Yes

COMET score: 0.87

HF link: https://huggingface.co/GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder submission-001

Training notebook: training/train.ipynb
Kaggle notebook URL: https://www.kaggle.com/code/yourname/submission-001
Dataset used: GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder train-001 (see DATASETS.md)

Docs updated: Yes
```

A complete PR description uses the repository PR template and provides the CI status, whether the interfaces are respected, the COMET score for model PRs, the Hugging Face link when required, and documentation status.

---

## 14. Where to ask

- Use **GitHub Issues** for bugs, scoped contribution requests, and questions that need to be tracked.
- Use **GitHub Discussions** for project-wide questions and conversations when Discussions are enabled.

Project maintainers and the project owner can be reached by opening an issue or participating in the relevant GitHub discussion. If a question contains private information or concerns a Code of Conduct report, use the reporting process in `CODE_OF_CONDUCT.md`.

---

## 15. CI, in one paragraph

Every pull request triggers an automated check defined in `.github/workflows/ci.yml`. It installs the root dependencies and runs `pytest tests/`. Green means the tests pass and the change is ready for review. Red means a test failed — fix it before asking for review.

GitHub runs this automatically on every push and pull request. You do not start it yourself.

Run `pytest tests/` on your own machine before you push. CI will catch what you miss, but it is faster to catch it locally.
