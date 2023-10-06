### Building Url Dynamically 


### Here I am importing Flask 
from flask import Flask

### I Create instance of Flask my instance name is app YOU may choose other
###Create an Instance of Flask
app=Flask(__name__)


### HOme page dirctory 
### /: This route corresponds to the home page of the web application. When you access the root URL (e.g., http://localhost:5000/),

@app.route('/')
def welcome():
    return "Welcome to IBM Faculty Development Program"


### This is my second directory when 
### This route corresponds to a page accessible at http://localhost:5000/Baiju. When you access this URL

@app.route('/Baiju')
def greet():
    return "Baiju kumar Here Welcome to all of you"


### Here I am assign main to my instance in conndition so that it will run my instance 
### starts the Flask development server with debugging enabled

if __name__=='__main__':
    app.run(debug=True)

