from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def admission_form():
    if request.method == 'POST':
        name = request.form['name']
        DOB = request.form['DOB']
        phone_number = request.form['phone_number']
        state = request.form['state']
        mark_12th = request.form['mark_12th']
        submitted = True
    
        #Pass the form data to the template
        return render_template('admissionform_9.html',
                               name=name,
                               DOB=DOB,
                               phone_number=phone_number,
                               state=state,
                               mark_12th=mark_12th,
                               submitted=submitted
                               )
    
    
    return render_template('admissionform_9.html')

if __name__=='__main__':
    app.run(debug=True)
