# Datasets

Single source of truth for datasets approved for use in this project. All dataset files live on the Hugging Face Hub, never in this Git repository.

## Phase Gate

A maximum of **20 approved training datasets**. Once 20 are approved, dataset collection closes. Further datasets need an explicit maintainer decision.

Test datasets do not count against the gate. A test set is infrastructure, not a contribution.

## Required Schema

Every dataset — training or test — uses exactly this structure:

```json
{
  "id": "1",
  "translation": {
    "eng_Latn": "I am a boy",
    "fra_Latn": "je suis un garçon"
  }
}
```

* `id`: unique string. No duplicates within a dataset.
* `translation.eng_Latn`: English source.
* `translation.fra_Latn`: French target.
* Language codes follow the NLLB-200 convention: [docs](https://huggingface.co/docs/transformers/model_doc/nllb).
* No extra keys. No renamed keys. No null values.

For test datasets, `translation.fra_Latn` is the reference translation COMET scores against.

## How to Add a Dataset

1. Prepare the dataset using the required schema.
2. Upload to the Hugging Face Hub under `GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder <dataset-name>`.
3. Confirm the repo contains the expected structure and metadata.
4. Open a pull request with the dataset reference and validation results.
5. CI checks the dataset schema.
6. A maintainer reviews, approves or rejects, and adds one row to the registry below on merge.

The number in the repo name is assigned by the maintainer at merge time. Propose a name in your PR; the maintainer assigns the final number. Do not assume your submission will keep the number you propose.

Do not add a row yourself. Do not add a status column. Rejected submissions never appear — the closed PR is the record.

## Dataset Registry

| Name | Repo | Subfolder | Contributor | Rows | Language pair | Type |
| --- | --- | --- | --- | ---: | --- | --- |
| English-French Parallel Sample | GDGBabcockUniversity/en-fr-train-001 | @club-member | 10000 | English → French | train |
| English-French News Sample | GDGBabcockUniversity/en-fr-train-002 | @hacktoberfest-contributor | 25000 | English → French | train |
| English-French Held-out Test Set | GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder test-v1 | @club-member | 2000 | English → French | test |

The rows above are examples showing the format. They are not real entries.

## Test Datasets

A test dataset is the held-out set used to score models. It is never trained on. See [MODELS.md](MODELS.md) → "What is the held-out test set?" for how it is used.

Test datasets follow the same schema and carry `type: test` in the registry.

`GDGBabcockUniversity-26/english_to_french_nmt_datasets` subfolder `test-v1` is the project's canonical test set. All model submissions report COMET against it, so scores are comparable across submissions. A contributor who wants a different test set must register it first and report both numbers in the PR.

A registered test set is frozen. Changing its contents invalidates every COMET score computed against it. To change a test set, register a new repository under a new name.

## Dataset Rules

* Never commit dataset files to Git.
* Store datasets on the Hugging Face Hub.
* Register each dataset repository as one row. Only a maintainer adds rows.
* Do not register the same repository more than once.
* Dataset IDs must be stable and reproducible.
* Keep the original source and licensing information in the Hugging Face repository.
* Do not modify an approved dataset silently. A materially changed dataset is submitted as a new version or repository.
* Approved datasets are not deleted from the registry. If a dataset should no longer be used, the maintainer opens a PR that removes the row and explains why.

## Review

Dataset contribution requirements and review rules are defined in [CONTRIBUTING.md](CONTRIBUTING.md). The dataset interface is part of the project's fixed interface contract. Changes to the required schema require maintainer approval.

## Related Documentation

* [CONTRIBUTING.md](CONTRIBUTING.md)
* [MODELS.md](MODELS.md)
* [NLLB-200 documentation](https://huggingface.co/docs/transformers/model_doc/nllb)
```