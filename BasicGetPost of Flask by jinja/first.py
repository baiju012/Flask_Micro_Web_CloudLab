from flask import Flask

app = Flask(__name__)

@app.route("/")
def first():
    return "Welcome to all the participant in CAD-FDP "

@app.route("/Baiju")
def home():
    return "Welcome to Home Page"


@app.route("/faculty")
def faculty():
    return "Faculty Development Program"

if __name__ == '__main__':
    app.run(debug=True)
