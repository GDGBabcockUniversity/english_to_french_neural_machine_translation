# Training

This folder contains two Jupyter notebooks:

- `train.ipynb` — trains a LoRA adapter on an English-French dataset.
- `eval.ipynb` — evaluates a trained adapter using COMET and reports scores.

## Run on Kaggle (recommended)

Kaggle provides free GPU compute. This is the supported path if you do not have a local GPU.

1. Create a free account at [kaggle.com](https://www.kaggle.com/).
2. Upload `train.ipynb` to Kaggle as a new notebook.
3. In the notebook sidebar, enable **Internet**.
4. Add your Hugging Face token as a Kaggle Secret named `HF_TOKEN`. To do this, open the notebook sidebar, select **Add-ons > Secrets**, and add the key.
5. Run all cells.

The notebook saves the adapter to `./models/` inside the Kaggle environment. After training, push the adapter to the Hugging Face Hub under `GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>`.

To evaluate, upload `eval.ipynb` to Kaggle the same way and run all cells.

## Run locally (requires a GPU)

1. Install dependencies:
2. Open `train.ipynb` in Jupyter and run all cells.
3. The adapter is saved to `./models/`.
4. Push the adapter to the Hugging Face Hub under `GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>`.
5. Open `eval.ipynb` and run all cells to get COMET scores.

## Where the adapter goes

After training, the adapter is saved locally to `./models/`. You then push it to the Hugging Face Hub under `GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>`.

See [MODELS.md](../MODELS.md) for what an adapter is and how it relates to the base model.

## Further reading

- [docs/model-guide.md](../docs/model-guide.md) — full walkthrough for training and submitting an adapter.
- [MODELS.md](../MODELS.md) — adapter registry and explanation of adapters.
- [docs/eval-guide.md](../docs/eval-guide.md) — how evaluation and scoring work.
