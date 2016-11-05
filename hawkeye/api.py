from flask import Flask, request, redirect, url_for
app = Flask(__name__)
from flask import render_template
import random

# Routes


@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/students/login/')
def students_login():
    return render_template('students-login.html')

@app.route("/students/home")
def user_home():
    user_reports = get_user_reports()
    return render_template('students-home.html', user_id=user_id, user_reports=user_reports)


@app.route("/submit-report")
def submit_report():
    form_id = int(round(random.random() * 10000000000))
    return render_template('submit-report.html',  user_id=user_id, form_id=form_id) 

@app.route("/view-bullying-reports")
def view_bullying_reports():
    show_id = request.args.get('msg_id')
    return render_template('view-bullying-reports.html', reports=reports, show_id=show_id)

@app.route('/counselors/login/')
def counselors_login():
    return render_template('counselors-login.html')

@app.route("/api/submit-report", methods=['POST'])
def handle_report_submit():
    data = request.form.to_dict()
    new_report = {
        'user_id': data['user_id'],
        'report_id': data['report_id'],
        'report_messages': [{
            'sender': 'student',
            'text': data['report_text']
        }]
    }
    reports.append(new_report)
    return '<p>Thank you for submitting a report, it has been forwarded anonymously to your counselor</p><a href="/students/home">Return Home</a>'

@app.route("/api/submit-reply-counselor", methods=['POST'])
def handle_reply_submit_c():
    data = request.form.to_dict()
    append_message_to_report(data)
    msg_id = data['user_id']
    return redirect(url_for('view_bullying_reports') + '?msg_id=' + msg_id)

@app.route("/api/submit-reply-student", methods=['POST'])
def handle_reply_submit_s():
    data = request.form.to_dict()
    append_message_to_report(data)
    return redirect(url_for('user_home'))

## Helpers
def append_message_to_report(data):
    for x in range(len(reports)):
        if reports[x]['report_id'] == data['report_id']:
            reports[x]['report_messages'].append({
                'sender': data['user_name'],
                'text': data['text']
            })

def get_user_reports():
    user_reports = []
    for report in reports:
        if report['user_id'] == str(user_id):
            user_reports.append(report)
    return user_reports

# Initialize state with some fake reports
user_id = int(round(random.random() * 10000))
reports = [
    {
        'user_id': 627,
        'report_id': 'a',
        'report_messages': [
            {'sender': 'student', 'text': 'I heard Cartman make fun of Stan\'s Jewish heritage.'},
            {'sender': 'counselor', 'text': 'When and where did you hear this?'},
        ],
    },
    {
        'user_id': 729,
        'report_id': 'b',
        'report_messages': [
            {'sender': 'student', 'text': 'I felt very upset when Cartman made fun of Kyle on Instagram.'},
            {'sender': 'counselor', 'text': 'Could you please send me the link to the post?'},
        ],
    }
]


# launch app

if __name__ == "__main__":
    app.run(debug=True)
