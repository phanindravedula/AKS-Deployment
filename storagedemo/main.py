from flask import Flask
app = Flask(__name__)

@app.route("/app3")
def hello():
    return "Hello from App3"
