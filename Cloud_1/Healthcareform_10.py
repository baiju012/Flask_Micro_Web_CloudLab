from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def health_insurance_form():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        pre_existing_conditions = 'Yes' if 'pre_existing_conditions' in request.form else 'No'
        phone_number=request.form['phone_number']
        height=request.form['height']
        weight=request.form['weight']
        submitted=True
    
        #Pass the form data to the template
        return render_template('Healthcareform_10.html',
                               name=name,
                               age=age,
                               pre_existing_conditions=pre_existing_conditions,
                               phone_number=phone_number,
                               height=height,
                               weight=weight,
                               submitted=submitted
                               )
    
    
    return render_template('Healthcareform_10.html')

if __name__=='__main__':
    app.run(debug=True)
