import test
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/get", methods=['POST'])
def get_bot_response():
    text = request.form['text']

    return render_template('index2.html', original_text=text, processed_text=test.bot(text))

if __name__ == "__main__":
    app.run()
