from flask import Flask
from threading import Thread


#Starting a Flask server on 0.0.0.0:8080
app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
