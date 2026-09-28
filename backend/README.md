# Backend

FastAPI service that translates English to French. Loads the fixed base model `facebook/nllb-200-distilled-1.3B` plus one approved adapter from the Hugging Face Hub. The frontend talks to this service. Nothing else loads model weights.

## Requirements

Git, Python 3.10+. A Hugging Face account is not required to run the backend.

## Setup

```bash
git clone https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git
cd english_to_french_neural_machine_translation

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -r backend/requirements.txt
```

## Configuration

Copy the template and fill it in:

```bash
cp .env.example .env
```

| Variable | Required | Meaning |
| --- | --- | --- |
| `ADAPTER_REPO` | yes | Hugging Face adapter repo ID. Must match a row in `MODELS.md`. |

The default is a placeholder. The server refuses to translate until you set a real value. `.env` is gitignored.

The base model is fixed and not configurable.

## Run

```bash
uvicorn backend.main:app --reload --port 8000
```

The model does not load at startup. It loads on the first `/translate` request (30–90 seconds, ~5 GB download). Later requests are fast.

Check it is up:

```bash
curl http://localhost:8000/health
```

## Endpoints

`GET /health` → `{"status": "ok"}`

`POST /translate`

```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

Request `{"text": "hello"}` → response `{"translation": "bonjour"}`

| Condition | Status |
| --- | --- |
| `text` missing, empty, or not a string | 400 |
| `text` exceeds 512 tokens | 400 |
| Model failed to load or translate | 500 |

Input over the limit is rejected, not truncated.

## How the model loads

Base model first, then the adapter on top: `PeftModel.from_pretrained(base, ADAPTER_REPO)`. The adapter is a small set of extra weights, not a standalone model. See [MODELS.md](../MODELS.md).

## Files

| File | Purpose |
| --- | --- |
| `main.py` | FastAPI app and routes. |
| `model.py` | Loads base + adapter, exposes `translate`. |
| `schemas.py` | Pydantic request/response models. |
| `config.py` | `BASE_MODEL`, `ADAPTER_REPO`, `MAX_LENGTH`. |
| `requirements.txt` | Backend dependencies. |

## Tests

```bash
pytest tests/
```

Tests mock the model. No download, no Hugging Face token needed.

## Review

`backend/` changes are **Medium** tier. Changes to `config.py` that alter `BASE_MODEL` or the response shape are **High** tier. See [CONTRIBUTING.md](../CONTRIBUTING.md) and [docs/interfaces.md](../docs/interfaces.md).

## Related

- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [MODELS.md](../MODELS.md)
- [docs/interfaces.md](../docs/interfaces.md)
```