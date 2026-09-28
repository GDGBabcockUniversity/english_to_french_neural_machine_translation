with open('MODELS.md', 'r', encoding='utf-8') as f:
    text = f.read()

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
text = text.replace("AutoModelForSeq2SeqLM.from_pretrained(adapter_id)", "AutoModelForSeq2SeqLM.from_pretrained(adapter_repo, subfolder=adapter_subfolder)")

with open('MODELS.md', 'w', encoding='utf-8') as f:
    f.write(text)
