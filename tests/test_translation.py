from translate.translation import Translator
import logging

def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        translator = Translator("facebook/mbart-large-50-many-to-many-mmt")
        translator.translate("Test sentence.",lang='German')
