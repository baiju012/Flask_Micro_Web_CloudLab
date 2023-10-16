from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def admission_form():
    if request.method == 'POST':
        name = request.form['name']
        DOB = request.form['DOB']
        phone_number = request.form['phone_number']
        state = request.form['state']
        mark_12th = int(request.form['mark_12th'])
        submitted = True

        eligible_for_admission = mark_12th > 400

        # Pass the form data to the template
        return render_template('admissionform.html',
                               name=name,
                               DOB=DOB,
                               phone_number=phone_number,
                               state=state,
                               mark_12th=mark_12th,
                               submitted=submitted,
                               eligible_for_admission=eligible_for_admission
                              
                               )

    return render_template('admissionform.html')


if __name__ == '__main__':
    app.run(debug=True)
