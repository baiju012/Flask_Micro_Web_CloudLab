from flask import Flask

app = Flask(__name__)

@app.route('/')


def welcome():
  return "welcome to HOme page of Fet of HOstal"


if __name__ =='__main__':
   app.run(debug=True)