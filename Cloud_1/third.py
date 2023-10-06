### Building Url Dynamically 


### Here I am importing Flask 
from flask import Flask

### I Create instance of Flask my instance name is app YOU may choose other
app=Flask(__name__)


### HOme page dirctory 
@app.route('/')

def welcome():
    return "Welcome to IBM Faculty Development Program"


### This is my second directory when 

@app.route('/Baiju')
def greet():
    return "Baiju kumar Here Welcome to all of you"


### Here I am assign main to my instance in conndition so that it will run my instance 
if __name__=='__main__':
    app.run(debug=True)

