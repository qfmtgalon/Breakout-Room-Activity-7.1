from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return ""

if __name__ == "__main__":
    app.run()
