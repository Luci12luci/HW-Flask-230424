from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Domovska stranka"

@app.route("/about")
def about():
    return "0 stranka"

if __name__ == "__main__":
    app.run()