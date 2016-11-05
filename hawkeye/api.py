from flask import Flask, request
app = Flask(__name__)
from flask import render_template

# Routes


@app.route("/")
def homepage():
    return render_template('homepage.html')
    '''
    <ol>
        <li><a href="/report-bullying">report bullying</a></li>
        <li><a href="/view-bullying-reports">view reports</a></li>
    </ol>
    '''

@app.route('/students/login/')
def students_login():
    return render_template('students-login.html')

@app.route('/counselors/login/')
def counselors_login():
    return render_template('counselors-login.html')

@app.route("/report-bullying")
def report_bullying():
    return render_template('report-bullying.html')

@app.route("/view-bullying-reports")
def view_report_bullying():
    return render_template('view-bullying-reports.html', reports=reports)

@app.route("/api/submit-report", methods=['POST'])
def handle_report_submit():
    data = request.form.to_dict()
    print (data)
    reports.append(data)
    return 'report submitted'

# State
reports = []





# launch app

if __name__ == "__main__":
    app.run(debug=True)