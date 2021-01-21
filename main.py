from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("game.html")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
