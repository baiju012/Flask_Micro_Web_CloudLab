from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('first.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 5000:
        res = "MORE"
    else:
        res = "LESS"
    return render_template('jinza.html', X=res)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        sallary_1 = float(request.form['sallary_1'])
        sallary_2 = float(request.form['sallary_2'])
        sallary_3 = float(request.form['sallary_3'])
        sallary_4 = float(request.form['sallary_4'])
        total_score = (sallary_1 + sallary_2 + sallary_3 + sallary_4) / 4
    return redirect(url_for('success', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)

