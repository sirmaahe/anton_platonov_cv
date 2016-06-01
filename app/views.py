from flask import *

from app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/cookies', methods=['GET'])
def cookies():
    return render_template('cookies.html')

if __name__ == '__main__':
    app.run(debug=True)
