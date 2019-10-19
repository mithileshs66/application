from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "MITHILESH KUMAR SHARMA - THE BOSS"


if __name__ == "__main__":
    app.run()
