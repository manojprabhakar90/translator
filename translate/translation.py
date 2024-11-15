import logging
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Configure logger
logger = logging.getLogger("TranslationLogger")
logger.setLevel(logging.INFO)

# Create console handler and set level to info
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add formatter to console handler
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

class Translator:
    # Define LANGUAGE_CODES as a class-level variable
    LANGUAGE_CODES = {
    "Arabic": "ar_AR", "Czech": "cs_CZ", "German": "de_DE", 
    "English": "en_XX", "Spanish": "es_XX", "Estonian": "et_EE",
      "Finnish": "fi_FI", "French": "fr_XX", "Gujarati": "gu_IN", 
      "Hindi": "hi_IN", "Italian": "it_IT", "Japanese": "ja_XX", 
      "Kazakh": "kk_KZ", "Korean": "ko_KR", "Lithuanian": "lt_LT", 
      "Latvian": "lv_LV", "Burmese": "my_MM", "Nepali": "ne_NP", 
      "Dutch": "nl_XX", "Romanian": "ro_RO", "Russian": "ru_RU", 
      "Sinhala": "si_LK", "Turkish": "tr_TR", "Vietnamese": "vi_VN", 
      "Chinese": "zh_CN", "Afrikaans": "af_ZA", "Azerbaijani": "az_AZ", 
      "Bengali": "bn_IN", "Persian": "fa_IR", "Hebrew": "he_IL", 
      "Croatian": "hr_HR", "Indonesian": "id_ID", "Georgian": "ka_GE", 
      "Khmer": "km_KH", "Macedonian": "mk_MK", "Malayalam": "ml_IN", 
      "Mongolian": "mn_MN", "Marathi": "mr_IN", "Polish": "pl_PL", 
      "Pashto": "ps_AF", "Portuguese": "pt_XX", "Swedish": "sv_SE", 
      "Swahili": "sw_KE", "Tamil": "ta_IN", "Telugu": "te_IN", "Thai": "th_TH", 
      "Tagalog": "tl_XX", "Ukrainian": "uk_UA", "Urdu": "ur_PK", "Xhosa": "xh_ZA", 
      "Galician": "gl_ES", "Slovene": "sl_SI"
    }

    def __init__(self, model_name: str):
        try:
            self.model_name = model_name
            self.model = MBartForConditionalGeneration.from_pretrained(self.model_name)
            self.tokenizer = MBart50TokenizerFast.from_pretrained(self.model_name)
            logger.info("Model and tokenizer loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading model or tokenizer: {e}")
            raise e

    def translate(self, text: str, lang: str):
        try:
            # Debugging: Print the language input and check mapping
            logger.info(f"Received language: {lang}")

            lang_code = None
            if lang in self.LANGUAGE_CODES:
                lang_code = self.LANGUAGE_CODES[lang]  # Language name to language code
                logger.info(f"Mapped language '{lang}' to language code '{lang_code}'")
            elif lang in self.LANGUAGE_CODES.values():
                lang_code = lang  # Language code already passed
                logger.info(f"Using language code '{lang_code}' directly")
            else:
                raise ValueError(f"Invalid language: {lang}")

            logger.info(f"Translating to {lang_code} ({lang})")

            # Tokenize the input text
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)

            # Translate
            translated = self.model.generate(
                inputs["input_ids"],
                forced_bos_token_id=self.tokenizer.lang_code_to_id[lang_code]  # Use lang_code for forced BOS token
            )

            # Decode the translated tokens back into text
            translation = self.tokenizer.decode(translated[0], skip_special_tokens=True)
            return translation

        except Exception as e:
            logger.error(f"Error during translation: {e}")
            raise e
