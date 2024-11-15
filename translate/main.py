from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from translate.translation import Translator  # Your existing translation class

app = FastAPI()

# Serve the index.html page
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize a default translator instance
translator = Translator(model_name="facebook/mbart-large-50-many-to-many-mmt")  # Using a single model for all languages

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/translate/")
async def translate_text(text: str, lang: str):
    try:
        # Since we're using the same model, there's no need to map languages to different models
        model_name = "facebook/mbart-large-50-many-to-many-mmt"  # Single model used for all languages
        translator.model_name = model_name  # Ensure the translator uses the correct model
        translator.tokenizer = Translator(model_name=model_name).tokenizer  # Update tokenizer for the model
        
        # Translate the text
        translated_text = translator.translate(text, lang)
        
        return {"original": text, "translated": translated_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during translation: {str(e)}")
