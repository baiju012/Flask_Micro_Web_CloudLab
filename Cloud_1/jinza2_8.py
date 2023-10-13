from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('indexjinza.html')

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
    total_score_av = 0
    if request.method == 'POST':
        salary_1 = float(request.form['salary_1'])
        salary_2 = float(request.form['salary_2'])
        salary_3 = float(request.form['salary_3'])
        salary_4 = float(request.form['salary_4'])
        total_score_av = (salary_1 + salary_2 + salary_3 + salary_4) / 4
    return redirect(url_for('success', score=total_score_av))

if __name__ == '__main__':
    app.run(debug=True)
