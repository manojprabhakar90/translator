from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from translate.translation import Translator  # Your existing translation class
from langdetect import detect  # For language detection
import langcodes  # For converting language codes to full names

app = FastAPI()

# Serve the index.html page
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize a default translator instance
translator = Translator(model_name="facebook/mbart-large-50-many-to-many-mmt")  # Single model for all languages

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/translate/")
async def translate_text(text: str, lang: str):
    try:
        detected_lang = detect(text)
        detected_lang_name =langcodes.Language.get(detected_lang).display_name() 
        translated_text = translator.translate(text, lang)
        return {
            "original": text,
            "detectedLanguage": detected_lang_name,
            "translated": translated_text,
            "targetLanguage": lang
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during translation: {str(e)}")
 