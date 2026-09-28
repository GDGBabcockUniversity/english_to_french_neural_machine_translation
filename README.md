
# GDG BABCOCK FRENCH-ENGLISH TRANSLATIONAL MODEL

> Fine-tune a multilingual model using LoRA/PEFT to outperform NLLB-200-1.3B (baseline) on COMET score for English→French translation, and expose it via a minimal FastAPI backend + HTML/JS frontend where users type English and receive French output.


## Table of Contents
- [What this project is](#what-this-project-is)
- [Architecture at a glance](#architecture-at-a-glance)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
  - [1. Clone the repository](#1-clone-the-repository)
  - [2. Create a virtual environment](#2-create-a-virtual-environment)
  - [3. Install dependencies](#3-install-dependencies)
  - [4. Create your environment file](#4-create-your-environment-file)
  - [5. Start the backend](#5-start-the-backend)
  - [6. Open the frontend](#6-open-the-frontend)
  - [7. Test a translation](#7-test-a-translation)
- [How to contribute](#how-to-contribute)
- [Datasets and models](#datasets-and-models)
- [Interface contract](#interface-contract)
- [Project streams](#project-streams)
- [License](#license)
- [Maintainers / contact](#maintainers--contact)

---

## What this project is

This project fine-tunes `facebook/nllb-200-distilled-1.3B` for English→French translation.
Contributors can add datasets, training experiments, evaluation improvements, backend changes, frontend changes, documentation, and infrastructure improvements.
The backend uses FastAPI to load an approved model from the Hugging Face Hub and expose a translation API.
The frontend provides a simple interface where a user enters English text and receives a French translation.
Models and datasets are hosted on the Hugging Face Hub rather than stored in this Git repository.

---

## Architecture at a glance

```text
Frontend
  ↓
Backend (FastAPI)
  ↓
Hugging Face Hub model

```

---

## Prerequisites

Install the following before starting:

* **Python**: Python 3.10 or newer
* **Git**: Git
* **Account**: A Hugging Face account 
* **Hardware**: A GPU is optional. CPU can be used for development and API testing; GPU hardware is recommended for fine-tuning.

---

## Quickstart

### 1. Clone the repository

```bash
git clone [https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git](https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git)
cd english_to_french_neural_machine_translation

```

### 2. Create a virtual environment

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Create your environment file

**Linux/macOS:**

```bash
cp .env.example .env

```

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env

```

> Open `.env` and set the Hugging Face model ID you want the backend to load.

### 5. Start the backend

From the repository root:

```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000

```

The API is now available at:

```text
[http://127.0.0.1:8000](http://127.0.0.1:8000)

```

### 6. Open the frontend

In a second terminal, from the repository root:

```bash
python -m http.server 3000 --directory frontend

```

Open:

```text
[http://127.0.0.1:3000](http://127.0.0.1:3000)

```

### 7. Test a translation

You can test the backend directly with:

```bash
curl -X POST [http://127.0.0.1:8000/translate](http://127.0.0.1:8000/translate) \
  -H "Content-Type: application/json" \
  -d '{"text": "I am a boy"}'

```

The response has this shape:

```json
{"translation": "je suis un garçon"}

```

The frontend uses the same `/translate` endpoint when you enter English text and submit it.

---

## How to contribute

Pick any stream that interests you; issues tagged `good-first-issue` are intended for beginner-friendly contributions.

Read the contribution rules before opening a pull request: CONTRIBUTING.md.

---

## Datasets and models

* **Datasets:** DATASETS.md — dataset contributions are tracked on the Hugging Face Hub; dataset collection closes at **20 approved repositories** for this phase.
* **Models:** MODELS.md — approved models are tracked on the Hugging Face Hub and evaluated using the project's fixed evaluation process.

---

## Interface contract

The project uses fixed data, training, API, and model interfaces so independent contributions can work together: docs/interfaces.md.

---

## Project streams

The project is divided into independent streams. Streams run in parallel, contributors can enter any stream, and work in one stream does not block work in another. For example, a new model can land while the frontend is still being styled.

* **Datasets** (`data/`)
* Collect, clean, and document English–French parallel corpora on the Hugging Face Hub.
* **Done** means the dataset follows the project schema, has documented provenance, is referenced by its HF Hub ID, and passes the required dataset checks. See `data/`.


* **Training** (`training/`)
* Run fine-tuning notebooks and reproducible hyperparameter experiments.
* **Done** means a training run saves an adapter to `./models/` and records the notebook settings and data reference needed to reproduce it. See `training/`.


* **Evaluation** (`tests/`)
* Maintain the evaluation harness, held-out test set, and scoring process used for submitted models.
* **Done** means a submitted model can be evaluated with the fixed harness and produces reproducible metrics for acceptance. See `tests/`.


* **Backend** (`backend/`)
* Build and maintain the FastAPI service that loads a model from the Hugging Face Hub and serves `/translate`.
* **Done** means the API follows the documented request/response contract and passes the backend tests. See `backend/`.


* **Frontend** (`frontend/`)
* Build the user interface for entering English text and receiving French translations.
* **Done** means a user can open the frontend, submit English text, and see the French response from the backend. See `frontend/`.


* **Docs** (`docs/`)
* Maintain setup instructions, architecture documentation, contribution guides, and onboarding material.
* **Done** means a beginner can follow the relevant documentation without needing undocumented project knowledge. See `docs/`.


* **Infra** (`.github/`)
* Maintain CI, issue and pull-request templates, repository configuration, and general repository hygiene.
* **Done** means project automation and repository conventions remain consistent and changes pass the required checks. See `.github/`.

