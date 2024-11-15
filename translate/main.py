from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from translate.translation import Translator

app = FastAPI()

# Initialize the translator
translator = Translator()

# Serve the index.html page
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/translate/")
async def translate_text(text: str):
    # Translate the text to German
    translated_text = translator.translate(text)  # Assuming the method can handle this
    return {"original": text, "translated": translated_text}
