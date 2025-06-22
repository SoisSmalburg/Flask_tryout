from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welkom! Deze site is gebouwd met Python door Sois Smalburg 👨‍💻</h1>"