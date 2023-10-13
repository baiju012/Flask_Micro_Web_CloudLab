#importing template by module of render_template and request to server
from flask import Flask,request, render_template

app=Flask(__name__)

@app.route('/')

def welcome():
  return render_template('post_6.html')



@app.route('/login',methods=['POST'])

def login():
     # Retrieve "uname" and "password" parameters from the form data.
    uname=request.form.get('uname')
    password=request.form.get('pass')
    if uname=='Baiju' and password=='Fet':
        return 'Welcome %s' %uname
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=True)

