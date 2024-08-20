from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        dest_language = request.form['language']
        translated = translator.translate(text, dest=dest_language)
        translated_text = translated.text

    return render_template('index.html', translated_text=translated_text, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
