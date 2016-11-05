from flask import Flask, request, redirect, url_for
app = Flask(__name__)
from flask import render_template
import random

# Routes

@app.route("/")
def homepage():
    return '''
    <ol>
        <li><a href="/user-home">report bullying</a></li>
        <li><a href="/view-bullying-reports">view reports</a></li>
    </ol>
    '''
@app.route("/user-home")
def user_home():
    user_reports = get_user_reports()
    print (user_reports)
    return render_template('user-home.html', user_id=user_id, user_reports=user_reports)

@app.route("/submit-report")
def submit_report():
    form_id = int(round(random.random() * 10000000000))
    return render_template('submit-report.html',  user_id=user_id, form_id=form_id) 

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
    return '<p>Thank you for submitting a report, it has been forwarded anonymously to your counselor</p><a href="/user-home">Return Home</a>'

@app.route("/api/submit-reply-counselor", methods=['POST'])
def handle_reply_submit_c():
    data = request.form.to_dict()
    append_message_to_report(data)
    return redirect(url_for('view_bullying_reports'))

@app.route("/api/submit-reply-student", methods=['POST'])
def handle_reply_submit_s():
    data = request.form.to_dict()
    append_message_to_report(data)
    return redirect(url_for('user_home'))

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

def get_user_reports():
    user_reports = []
    print (reports)
    print (user_id)
    for report in reports:
        if report['user_id'] == str(user_id):
            user_reports.append(report)
    return user_reports

# State
user_id = int(round(random.random() * 10000))
reports = []


# launch app

if __name__ == "__main__":
    app.run(debug=True)