# Setup

Get the project running on your machine. Follow top to bottom. Every command is copy-pasteable.

This covers the backend and the frontend. Training is not here — training runs on Kaggle, see [docs/model-guide.md](model-guide.md).

## Prerequisites

- Git
- Python 3.10 or newer
- A GitHub account

A Hugging Face account is **not** required. Create one only if you plan to contribute a dataset or an adapter.

Check your Python version:

```bash
python --version
```

If it prints less than 3.10, install a newer Python before continuing.

## 1. Clone the repository

```bash
git clone https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git
cd english_to_french_neural_machine_translation
```

## 2. Create a virtual environment

A virtual environment keeps this project's packages separate from your system Python. Without it, installing this project's packages can break other Python projects on your machine.

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate          # macOS, Linux
.venv\Scripts\activate             # Windows
```

Your terminal prompt now starts with `(.venv)`. You must activate the environment every time you open a new terminal for this project.

## 3. Install dependencies

Two files. Install both.

```bash
pip install -r requirements.txt
pip install -r backend/requirements.txt
```

Training dependencies are not installed here. If you train an adapter, the notebook installs what it needs when it runs.

## 4. Configure the backend

The backend reads its adapter ID from a file named `.env`. That file is not in the repo — it is gitignored, because it can hold a secret later.

Copy the template:

```bash
cp .env.example .env
```

Open `.env` in a text editor. Set `ADAPTER_REPO` to a real adapter repo ID from [MODELS.md](../MODELS.md):

```
ADAPTER_REPO=GDGBabcockUniversity-26/english_to_french_nmt_adapters
ADAPTER_SUBFOLDER=submission-001
```

The template contains a placeholder. The server refuses to translate until you set a real value. This is on purpose — a fake default would fail later with a confusing error.

## 5. Run the backend

From the repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

Leave this terminal open.

The server starts immediately. The model does not load yet. It loads on the first `/translate` request, which takes 30 to 90 seconds and downloads about 5 GB from the Hugging Face Hub. The first translation will feel slow. Every request after that is fast.

## 6. Verify it works

Open a second terminal. Check the server is up:

```bash
curl http://localhost:8000/health
```

Expected: `{"status":"ok"}`

Now send a translation:

```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

Expected: `{"translation":"bonjour"}`

The first call to `/translate` waits for the model to load. Give it a minute. If it returns, the backend is working.

## 7. Open the frontend

Open a third terminal.

```bash
cd frontend
python -m http.server 5500
```

Open `http://localhost:5500` in your browser.

The frontend talks to the backend at `http://localhost:8000`. Both must be running at the same time.

Type English into the input box. French appears in the output box.

## Common problems

**`command not found: python`**
Try `python3` instead. Some systems only expose the versioned name.

**`ModuleNotFoundError`**
The virtual environment is not active. Run the activate command from step 2 again. Your prompt must show `(.venv)`.

**`Address already in use`**
Port 8000 or 5500 is taken by another process. Stop it, or use a different port:

```bash
uvicorn backend.main:app --reload --port 8001
python -m http.server 5501
```

If you change a port, every command and every URL must use the new one.

**`ADAPTER_REPO is still a placeholder`**
You skipped step 4, or you did not replace the placeholder value. Open `.env` and set a real adapter repo ID.

**The first translation takes forever**
That is expected. The model is downloading. Watch the backend terminal — progress is printed there. Every call after the first is fast.

**The frontend shows a CORS error**
The backend is not running, or it is on a different port. Check step 5.

**Model download fails**
You may be behind a network that blocks the Hugging Face Hub. Try again on a different connection.

## What next

- Run the tests: `pytest tests/`
- Read the contract: [docs/interfaces.md](interfaces.md)
- Train an adapter on Kaggle: [docs/model-guide.md](model-guide.md)
- Understand the system: [docs/architecture.md](architecture.md)

## Related Documentation

- [README.md](../README.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [backend/README.md](../backend/README.md)
- [docs/interfaces.md](interfaces.md)
- [docs/architecture.md](architecture.md)
```