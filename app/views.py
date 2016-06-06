from flask import *

from app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/cookies', methods=['GET'])
def cookies():
    return render_template('cookies.html')


@app.route('/zeynalov/cookies', methods=['GET'])
def zeynalov_cookies():
    return render_template('zeynalov/cookies.html')


@app.route('/zeynalov/resume', methods=['GET'])
def zeynalov_resume():
    return render_template('zeynalov/resume.html')

if __name__ == '__main__':
    app.run(debug=True)
