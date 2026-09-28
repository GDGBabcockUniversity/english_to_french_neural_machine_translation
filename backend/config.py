import os
from dotenv import load_dotenv

load_dotenv()

# Fixed base model. Do not change. Every adapter in this project targets this model.
BASE_MODEL = "facebook/nllb-200-distilled-1.3B"

# Adapter to load on top of the base model.
# Set in .env. Must match a row in MODELS.md.
ADAPTER_REPO = os.getenv("ADAPTER_REPO") or "GDGBabcockUniversity-26/english_to_french_nmt_adapters"
ADAPTER_SUBFOLDER = os.getenv("ADAPTER_SUBFOLDER") or "submission-001"

# Maximum input length in tokens. This is NLLB's hard cap.
# Input exceeding this is rejected with HTTP 400, not truncated.
MAX_LENGTH = 512