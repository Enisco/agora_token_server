from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Flask App for Agora Token Client."