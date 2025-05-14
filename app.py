from flask import Flask, render_template, request, redirect, url_for, flash
from googletrans import Translator
translator = Translator()
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        result= translator.translate(text, target_language)
        return render_template('index.html', translated_text=result.text)
if __name__ == '__main__':
    app.run(debug=True)