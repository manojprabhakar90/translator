from translate.translation import Translator
import logging

def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        translator = Translator("facebook/mbart-large-50-many-to-many-mmt")
        translator.translate("Test sentence.",lang='German')
    assert "Initializing translator with model" in caplog.text
    assert "Translation completed successfully" in caplog.text
