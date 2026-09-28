import os

def p_global(text):
    text = text.replace('https://github.com/GDG-Babcock/english-french-translator.git', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git')
    text = text.replace('https://github.com/GDG-Babcock/english-french-translator', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation')
    text = text.replace('https://github.com/GDG-Babcock/nllb-en-fr.git', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git')
    text = text.replace('https://github.com/GDG-Babcock/nllb-en-fr', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation')
    text = text.replace('https://github.com/GDG-Babcock/french_english_translator.git', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git')
    text = text.replace('https://github.com/GDG-Babcock/french_english_translator', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation')
    text = text.replace('https://github.com/YOUR-CLUB/english-french-translator.git', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation.git')
    text = text.replace('https://github.com/YOUR-CLUB/english-french-translator', 'https://github.com/GDGBabcockUniversity/english_to_french_neural_machine_translation')

    text = text.replace('cd english-french-translator', 'cd english_to_french_neural_machine_translation')
    text = text.replace('cd nllb-en-fr', 'cd english_to_french_neural_machine_translation')
    text = text.replace('cd french_english_translator', 'cd english_to_french_neural_machine_translation')
    text = text.replace('cd french-english-translator', 'cd english_to_french_neural_machine_translation')

    text = text.replace('the GDG-Babcock GitHub org', 'the GDGBabcockUniversity GitHub org')
    
    text = text.replace('GDG-Babcock/english-french-translator', 'GDGBabcockUniversity/english_to_french_neural_machine_translation')
    return text

def process_file(filepath):
    if not os.path.exists(filepath) and filepath != '.env.example': return False
    if filepath == '.env.example':
        new_content = 'ADAPTER_REPO=GDGBabcockUniversity-26/english_to_french_nmt_adapters\nADAPTER_SUBFOLDER=submission-001\n'
        with open(filepath, 'w', encoding='utf-8') as f: f.write(new_content)
        return True

    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()

    orig = content
    text = p_global(content)

    if filepath == 'architecture.md':
        text = text.replace('GDGBabcockUniversity/en-fr-test-v1', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder test-v1')
        text = text.replace('huggingface.co/GDGBabcockUniversity)', 'huggingface.co/GDGBabcockUniversity-26)')
        text = text.replace('GDGBabcockUniversity organization', 'GDGBabcockUniversity-26 organization')
        text = text.replace('HF Hub, `GDGBabcockUniversity/`', 'HF Hub, `GDGBabcockUniversity-26/`')
        text = text.replace('HF Hub\n(GDGBabcockUniversity/...)', 'HF Hub\n(GDGBabcockUniversity-26/...)')

    elif filepath == 'CONTRIBUTING.md':
        text = text.replace('YOUR-CLUB/en-fr-train-001', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder train-001')
        text = text.replace('YOUR-CLUB/nllb-en-fr-submission-001', 'GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder submission-001')
        text = text.replace('huggingface.co/YOUR-CLUB/nllb-en-fr-submission-001', 'huggingface.co/GDGBabcockUniversity-26/english_to_french_nmt_adapters/tree/main/submission-001')
        text = text.replace('nllb-en-fr-submission-001', 'submission-001')
        text = text.replace('en-fr-train-001 (see DATASETS.md)', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder train-001 (see DATASETS.md)')

    elif filepath == 'DATASETS.md':
        text = text.replace('GDGBabcockUniversity/<dataset-name>', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder <dataset-name>')
        text = text.replace('| Name | Hugging Face repo ID | Contributor | Rows | Language pair | Type |', '| Name | Repo | Subfolder | Contributor | Rows | Language pair | Type |')
        text = text.replace('| --- | --- | --- | ---: | --- | --- |', '| --- | --- | --- | --- | ---: | --- | --- |')
        text = text.replace('| English-French Parallel Sample | GDGBabcockUniversity/en-fr-train-001 | @club-member | 10000 | English ? French | train |', '| English-French Parallel Sample | GDGBabcockUniversity-26/english_to_french_nmt_datasets | train-001 | @club-member | 10000 | English ? French | train |')
        text = text.replace('| English-French News Sample | GDGBabcockUniversity/en-fr-train-002 | @hacktoberfest-contributor | 25000 | English ? French | train |', '| English-French News Sample | GDGBabcockUniversity-26/english_to_french_nmt_datasets | train-002 | @hacktoberfest-contributor | 25000 | English ? French | train |')
        text = text.replace('| English-French Held-out Test Set | GDGBabcockUniversity/en-fr-test-v1 | @club-member | 2000 | English ? French | test |', '| English-French Held-out Test Set | GDGBabcockUniversity-26/english_to_french_nmt_datasets | test-v1 | @club-member | 2000 | English ? French | test |')
        text = text.replace('`GDGBabcockUniversity/en-fr-test-v1`', '`GDGBabcockUniversity-26/english_to_french_nmt_datasets` subfolder `test-v1`')
        text = text.replace('GDGBabcockUniversity/en-fr-test-v1', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder test-v1') # Fallback

    elif filepath == 'MODELS.md':
        text = text.replace('GDGBabcockUniversity organization', 'GDGBabcockUniversity-26 organization')
        text = text.replace('repository ID, under `GDGBabcockUniversity`', 'repository ID, under `GDGBabcockUniversity-26`')
        text = text.replace('GDGBabcockUniversity/<adapter-name>', 'GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>')
        text = text.replace('| Name | Repo | Contributor | Base COMET | Fine-tuned COMET | Train dataset (rows) | Test dataset (rows) |', '| Name | Repo | Subfolder | Contributor | Base COMET | Fine-tuned COMET | Train dataset (rows) | Test dataset (rows) |')
        text = text.replace('| --- | --- | --- | --- | --- | --- | --- |', '| --- | --- | --- | --- | --- | --- | --- | --- |')
        text = text.replace('| NLLB English-French Baseline Adapter | GDGBabcockUniversity/nllb-en-fr-submission-001 | @club-member | 0.82 | 0.87 | en-fr-train-001 (50,000) | en-fr-test-v1 (2,000) |', '| NLLB English-French Baseline Adapter | GDGBabcockUniversity-26/english_to_french_nmt_adapters | submission-001 | @club-member | 0.82 | 0.87 | train-001 (50,000) | test-v1 (2,000) |')
        text = text.replace('| NLLB English-French Experiment 02 | GDGBabcockUniversity/nllb-en-fr-submission-002 | @hacktoberfest-contributor | 0.82 | 0.89 | en-fr-train-002 (30,000) | en-fr-test-v1 (2,000) |', '| NLLB English-French Experiment 02 | GDGBabcockUniversity-26/english_to_french_nmt_adapters | submission-002 | @hacktoberfest-contributor | 0.82 | 0.89 | train-002 (30,000) | test-v1 (2,000) |')
        old_load = """adapter_id = "GDGBabcockUniversity/nllb-en-fr-submission-001"       # a row from the registry above

tokenizer = AutoTokenizer.from_pretrained(base_id)
base = AutoModelForSeq2SeqLM.from_pretrained(base_id)
model = PeftModel.from_pretrained(base, adapter_id)"""
        new_load = """adapter_repo = "GDGBabcockUniversity-26/english_to_french_nmt_adapters"
adapter_subfolder = "submission-001"

tokenizer = AutoTokenizer.from_pretrained(base_id)
base = AutoModelForSeq2SeqLM.from_pretrained(base_id)
model = PeftModel.from_pretrained(
    base,
    adapter_repo,
    subfolder=adapter_subfolder
)"""
        text = text.replace(old_load, new_load)
        text = text.replace('AutoModelForSeq2SeqLM.from_pretrained(adapter_id)', 'AutoModelForSeq2SeqLM.from_pretrained(adapter_repo, subfolder=adapter_subfolder)')

    elif filepath == 'README.md':
        text = text.replace('GDGBabcockUniversity/<adapter-name>', 'GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>')

    elif filepath == '.github/PULL_REQUEST_TEMPLATE.md':
        text = text.replace('Adapter repo ID: GDGBabcockUniversity/nllb-en-fr-submission-001', 'Adapter repo ID: GDGBabcockUniversity-26/english_to_french_nmt_adapters\nSubfolder: submission-001')
        text = text.replace('nllb-en-fr-submission-001', 'submission-001')

    elif filepath == 'backend/config.py':
        old_adapter = 'ADAPTER_REPO = os.getenv("ADAPTER_REPO") or "GDGBabcockUniversity/<adapter-name>"'
        new_adapter = 'ADAPTER_REPO = os.getenv("ADAPTER_REPO") or "GDGBabcockUniversity-26/english_to_french_nmt_adapters"\nADAPTER_SUBFOLDER = os.getenv("ADAPTER_SUBFOLDER") or "submission-001"'
        text = text.replace(old_adapter, new_adapter)

    elif filepath == 'backend/model.py':
        text = text.replace('self.model = PeftModel.from_pretrained(base, config.ADAPTER_REPO )', 'self.model = PeftModel.from_pretrained(\n            base,\n            config.ADAPTER_REPO,\n            subfolder=config.ADAPTER_SUBFOLDER\n        )')

    elif filepath == 'backend/README.md':
        text = text.replace('ADAPTER_REPO=GDGBabcockUniversity/nllb-en-fr-submission-001', 'ADAPTER_REPO=GDGBabcockUniversity-26/english_to_french_nmt_adapters\nADAPTER_SUBFOLDER=submission-001')

    elif filepath == 'docs/dataset-guide.md':
        text = text.replace('GDGBabcockUniversity/<dataset-name>', 'GDGBabcockUniversity-26/english_to_french_nmt_datasets subfolder <dataset-name>')

    elif filepath == 'docs/setup.md':
        text = text.replace('ADAPTER_REPO=GDGBabcockUniversity/nllb-en-fr-submission-001', 'ADAPTER_REPO=GDGBabcockUniversity-26/english_to_french_nmt_adapters\nADAPTER_SUBFOLDER=submission-001')

    elif filepath == 'docs/interfaces.md':
        text = text.replace('PeftModel.from_pretrained(base, adapter_id)', 'PeftModel.from_pretrained(\n    base,\n    "GDGBabcockUniversity-26/english_to_french_nmt_adapters",\n    subfolder="submission-001",\n)')

    elif filepath == 'training/README.md':
        text = text.replace('GDGBabcockUniversity/<adapter-name>', 'GDGBabcockUniversity-26/english_to_french_nmt_adapters subfolder <adapter-name>')

    if text != orig:
        with open(filepath, 'w', encoding='utf-8') as f: f.write(text)
        return True
    return False

files = [
    'architecture.md',
    'CONTRIBUTING.md',
    'DATASETS.md',
    'MODELS.md',
    'README.md',
    '.github/PULL_REQUEST_TEMPLATE.md',
    'backend/config.py',
    'backend/model.py',
    'backend/README.md',
    'docs/dataset-guide.md',
    'docs/setup.md',
    'docs/interfaces.md',
    'training/README.md',
    '.env.example'
]

for f in files:
    process_file(f)

