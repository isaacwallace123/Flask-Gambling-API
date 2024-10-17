from flask import Flask, Blueprint

from deck import DeckApp

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(DeckApp)

@app.route("/", methods=["GET"])
def main():
    return "Hello World"

@app.errorhandler(404)
def NotFoundException(Error):
    return Error

if __name__ == "__main__":
    app.run()