from flask import Flask
app = Flask(__name__)

@app.route("/")
def app():
    return "Hello Flask, on Azure App Service for Linux"