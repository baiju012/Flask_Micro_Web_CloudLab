# In this we will see get and post together with same url diffrence

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template('getpost.html')


# Define a route that requires both GET and POST requests
@app.route('/submit', methods=['GET', 'POST'])
def example_form():
    if request.method == 'GET':
        # Handle GET requests (display the form)
        name = request.args.get('name')
         # f before the string, which denotes an f-string in Python. This allows you to embed the value of the name variable within the string.
        return f'Hi there, {name}! Thank you for submitting the form.'

    if request.method == 'POST':
        # Handle POST requests (form submission)
        name = request.form.get('name')
        # f before the string, which denotes an f-string in Python. This allows you to embed the value of the name variable within the string.
        return f'Hi there, {name}! Thank you for submitting the form.'

if __name__ == '__main__':
    app.run(debug=True)
