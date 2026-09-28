from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel

from backend import config

class Translator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(config.BASE_MODEL)
        base = AutoModelForSeq2SeqLM.from_pretrained(config.BASE_MODEL)
        self.model = PeftModel.from_pretrained(
            base,
            config.ADAPTER_REPO,
            subfolder=config.ADAPTER_SUBFOLDER
        )
        self.model.eval()

    def translate(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=config.MAX_LENGTH)
        outputs = self.model.generate(**inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id["fra_Latn"])
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)