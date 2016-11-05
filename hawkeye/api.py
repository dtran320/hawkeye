from flask import Flask, request
app = Flask(__name__)
from flask import render_template
import random

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
    rand_num = int(round(random.random() * 10000))
    return render_template('report-bullying.html', id=rand_num)

@app.route("/view-bullying-reports")
def view_report_bullying():
    return render_template('view-bullying-reports.html', reports=reports) 

@app.route("/api/submit-report", methods=['POST'])
def handle_report_submit():
    data = request.form.to_dict()
    print data
#    new_report = {
#        id: data.id
#    }
    reports.append(data)
    return 'report submitted'

# State
reports = []




# launch app

if __name__ == "__main__":
    app.run(debug=True)