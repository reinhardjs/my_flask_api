from flask import Flask

app = Flask(__name__)
#asd
@app.route("/hello")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")
