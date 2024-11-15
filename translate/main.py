from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from translate.translation import Translator  # Your existing translation class

app = FastAPI()

# Mapping of languages to model names
model_mapping = {
    "de": "facebook/mbart-large-50-many-to-many-mmt",  # German model
    "mr": "facebook/mbart-large-50-many-to-many-mmt",  # Marathi model (same model, adjust accordingly)
    "fr": "facebook/mbart-large-50-many-to-many-mmt",  # French model (same model, adjust accordingly)
}

# Serve the index.html page
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/translate/")
async def translate_text(text: str, lang: str):
    # Select the model based on the target language
    model_name = model_mapping.get(lang, "facebook/mbart-large-50-many-to-many-mmt")
    translator = Translator(model_name=model_name)
    
    # Translate the text
    translated_text = translator.translate(text, target_lang=lang)
    
    return {"original": text, "translated": translated_text}
