from flask import Flask, request, redirect, url_for
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
    user_id = int(round(random.random() * 10000))
    form_id = int(round(random.random() * 10000000000))
    return render_template('report-bullying.html', user_id=user_id, form_id=form_id)

@app.route("/view-bullying-reports")
def view_bullying_reports():
    return render_template('view-bullying-reports.html', reports=reports) 

@app.route("/api/submit-report", methods=['POST'])
def handle_report_submit():
    data = request.form.to_dict()
    print (data)
    new_report = {
        'user_id': data['user_id'], 
        'report_id': data['report_id'],
        'report_messages': [{
            'sender': 'student',
            'text': data['report_text']
        }]
    }
    reports.append(new_report)
    print (reports)
    return 'Thank you for submitting a report, it has been forwarded anonymously to your counselor'

@app.route("/api/submit-reply", methods=['POST'])
def handle_reply_submit():
    data = request.form.to_dict()
    append_message_to_report(data)
    return redirect(url_for('view_bullying_reports'))

## Helpers
def append_message_to_report(data):
    for x in range(len(reports)):
        if reports[x]['report_id'] == data['report_id']:
            print ('in this if')
            reports[x]['report_messages'].append({
                'sender': data['user_name'],
                'text': data['text']
            })
    print ('new report data')
    print (reports)

# State
reports = []


# launch app

if __name__ == "__main__":
    app.run(debug=True)