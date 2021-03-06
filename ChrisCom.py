from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pull_astros_info import pull_score,interpret_score
from smtplib import SMTP
from email.mime.text import MIMEText
from time import time

with open('emailinfo', 'r') as f:
# with open('C:\\Users\\chris_000\\PycharmProjects\\ChrisCom\\emailinfo', 'r') as f:
    email_info = f.readlines()
    email_user = email_info[0].strip()
    email_pwd = email_info[1].strip()

server_start_time = time()
app = Flask(__name__)
app.secret_key = 'some_secret_that_you_do_not_know'


@app.route('/')
@app.route('/home')
def home_page():
    server_uptime = int(time()-server_start_time)
    meme_url=open('static/misc/meme_url.txt','r').read()
    game_info = interpret_score(pull_score())
    return render_template(
        'home_page.html',
        gameinfo=game_info,
        server_uptime=server_uptime,
        meme_url=meme_url)

@app.route('/about')
def about_page():
    return render_template('about_page.html')


@app.route('/contact')
def contact_page():
    return render_template('contact_page.html')


@app.route('/projects')
def projects_page():
    return render_template('projects_page.html')


@app.route('/resume')
def resume_page():
    return render_template('resume_page.html')

@app.route('/stat_405')
def stat_405():
    return render_template('stat_405.html')

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    message = request.form.to_dict()
    if message['User_Name'] == '':
        message['User_Name'] = 'Anonymous User'

    s = SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(email_user, email_pwd)

    msg = MIMEText(
        'They sent you this message on chris.com- \n \n' +
        message['Comment'],
        'plain')
    msg['Subject'] = message['User_Name'] + ' sent you a message on chris.com'
    msg['From'] = email_user

    s.sendmail(email_user, 'christopherthomas55@gmail.com', msg.as_string())
    flash('Message submitted succesfully!')
    return redirect(url_for('contact_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
