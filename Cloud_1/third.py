from flask import Flask

app=Flask(__name__)

@app.route('/')

def welcome():
    return "Welcome to IBM Faculty Development Program"

@app.route('/Baiju')
def greet():
    return "Baiju kumar Here Welcome to all of you"

if __name__=='__main__':
    app.run(debug=True)

