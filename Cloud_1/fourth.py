### Building Url Dynamically 
####Variable Rules And URL Building



### Here I am importing Flask and for building of dynamic url you have to use redirect and url_for

from flask import Flask,redirect,url_for

### I Create instance of Flask my instance name is app YOU may choose other
app=Flask(__name__)


### This route is for HOme Page

@app.route('/')
def welcome():
    return "Welcome to my Home Page"


### You may use variable parameter in route    
###You may provide html whole file or small code

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Reult is passed</h1></body></html>"


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker using redirect url
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

###Here I am assign main to my instance in conndition so that it will run my instance 
if __name__=='__main__':
    app.run(debug=True)
