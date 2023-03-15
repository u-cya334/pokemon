from flask import Flask,request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shiritori.html")
def shiritori():
    return render_template("shiritori.html")

if __name__ == "__main__":
    app.run(debug=True)
