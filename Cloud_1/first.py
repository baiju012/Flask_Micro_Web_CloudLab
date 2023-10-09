# Basic web application of flask going to run on web server 


from flask import Flask

app = Flask(__name__)

@app.route('/')


def welcome():
  return "welcome to Home page of Fet."

###Here I am assign main to my instance in conndition so that it will run my instance 
if __name__ =='__main__':
   app.run(debug=False)
