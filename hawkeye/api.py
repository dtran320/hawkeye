from flask import Flask
app = Flask(__name__)
from flask import render_template

# Routes

@app.route("/")
def homepage():
    return '''
    <ol>
        <li><a href="/report-bullying">report bullying</a></li>
        <li><a href="/view-bullying-reports">view reports</a></li>
    </ol>
    '''
@app.route("/report-bullying")
def report_bullying():
    return render_template('report-bullying.html')

@app.route("/view-bullying-reports")
def view_report_bullying():
    return render_template('view-bullying-reports.html', reports=reports) 

@app.route("/api/submit-report")
def handle_report_submit():
    print 'report submitted'
    return 'report submitted'

# State
reports = ['report 1', 'report 2']





# launch app

if __name__ == "__main__":
    app.run(debug=True)