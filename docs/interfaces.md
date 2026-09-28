# Interface Contract

This document defines the fixed interfaces in this project. Independent contributions rely on these contracts staying stable.

---

## 1. Data row

Each dataset row is `{"id": str, "translation": {"eng_Latn": str, "fra_Latn": str}}`. No extra keys, no renamed keys, no null values.

---

## 2. Training

Training is run by opening `training/train.ipynb` and running all cells. It saves the adapter to `./models/`.

---

## 3. Model loading

Must be a seq2seq model loadable via `AutoModelForSeq2SeqLM.from_pretrained(...)` with an NLLB tokenizer. No classification heads, no custom architectures. Adapters are loaded on top of the base model using `PeftModel.from_pretrained(
    base,
    "GDGBabcockUniversity-26/english_to_french_nmt_adapters",
    subfolder="submission-001",
)`.

---

## 4. API

`POST /translate` with body `{"text": "hello"}` returns `{"translation": "bonjour"}`. Missing or empty text returns 400. Model failure returns 500. No other fields.
