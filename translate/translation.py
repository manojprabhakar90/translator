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
    def __init__(self,model_name="facebook/mbart-large-50-many-to-many-mmt"):
        """
        Initializes the translator with self command.
        """
        logger.info(f"Initializing translator with model: {model_name}")
        try:
            self.tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
            self.model = MBartForConditionalGeneration.from_pretrained(model_name)
            logger.info("Model and tokenizer loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading model/tokenizer: {e}")
            raise

    def translate(self, text: str) -> str:
        """
        Translates the input text using the Bart model.

        Args:
            text (str): The input text to translate.

        Returns:
            str: Translated text.
        """
        logger.info(f"Translating text: {text}")
        try:
            # Tokenize input text
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            logger.debug(f"Tokenized inputs: {inputs}")

            # Generate output
            outputs = self.model.generate(**inputs)
            logger.info("Translation completed successfully.")

            # Decode and return the translated text
            result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            logger.info(f"Translated text: {result}")
            return result
        except Exception as e:
            logger.error(f"Error during translation: {e}")
            raise
