# Basic web application of flask going to run on web server runable form enable.
from flask import Flask

app = Flask(__name__)

@app.route('/')


def welcome():
  return "welcome to Home page of Fet."


if __name__ =='__main__':
   app.run(debug=True)
