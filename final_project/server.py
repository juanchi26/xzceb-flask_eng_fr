from machinetranslation import traslator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text_traslated = traslator.english_to_french(textToTranslate)
    return text_traslated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    text_traslated = traslator.french_to_english(textToTranslate)
    return text_traslated

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
