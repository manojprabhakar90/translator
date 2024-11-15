from translate.translation import Translator
import logging

def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        translator = Translator()
        translator.translate("Test sentence.")
    assert "Initializing translator with model" in caplog.text
    assert "Translation completed successfully" in caplog.text
