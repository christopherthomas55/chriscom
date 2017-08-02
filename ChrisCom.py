from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home_page.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
