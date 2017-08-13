from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pull_astros_info import *
from smtplib import SMTP
from email.mime.text import MIMEText
from time import time

<<<<<<< HEAD
with open('/home/chris_files/chriscom/emailinfo', 'r') as f:
    # with open('C:\\Users\\chris_000\\PycharmProjects\\ChrisCom\\emailinfo',
    # 'r') as f:
    email_info = f.readlines()
=======
#with open('/home/chris_files/chriscom/emailinfo','r') as f:
with open('C:\\Users\\chris_000\\PycharmProjects\\ChrisCom\\emailinfo', 'r') as f:
    email_info=f.readlines()
>>>>>>> b15f4e36fd305f23493c8347f1634d5e3133b7b3
    email_user = email_info[0]
    email_pwd = email_info[1]

server_start_time = time()
app = Flask(__name__)
app.secret_key = 'some_secret_that_you_do_not_know'


@app.route('/')
@app.route('/home')
def home_page():
    server_uptime = int(time()-server_start_time)
<<<<<<< HEAD
    return render_template(
        'home_page.html',
        server_uptime=server_uptime,
        meme_url=open(
            '/home/chris_files/chriscom/static/misc/meme_url.txt',
            'r').read())
    # return render_template('home_page.html', server_uptime=server_uptime,
    # meme_url=open('C:/Users/chris_000/PycharmProjects/ChrisCom/static/misc/meme_url.txt','r').read())

=======
    game_info = interpret_score(pull_score())
    #return render_template('home_page.html', server_uptime=server_uptime, meme_url=open('/home/chris_files/chriscom/static/misc/meme_url.txt','r').read())
    return render_template('home_page.html', gameinfo=game_info, server_uptime=server_uptime, meme_url=open('C:/Users/chris_000/PycharmProjects/ChrisCom/static/misc/meme_url.txt','r').read())
>>>>>>> b15f4e36fd305f23493c8347f1634d5e3133b7b3

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
