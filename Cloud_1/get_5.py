#both "GET" and "POST" can send data to the server

#importing a template from flask module of render_template
from flask import Flask,request, render_template

app=Flask(__name__)


@app.route('/')

def welcome():
  return render_template('get_5.html')  # for this html go to templates folder in this repository



# Define a route for the root URL ("/") that handles GET requests.
# handles GET requests and retrieves a "uname" parameter from the query string.
# the 'methods' attribute allowed for particular route on the server-side 
# while the 'method' attribute in HTML specifies how the form data should be sent to the server when submitted from the client-side.

@app.route('/login',methods=['GET'])
def login():
    # Get the "uname" parameter from the query string.
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='Baiju' and password=='Fet':
        return 'Welcome %s' %uname
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=True)

