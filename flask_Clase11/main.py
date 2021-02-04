from flask import Flask
from flask import render_template

import forms # forms.py

app = Flask(__name__)

@app.route('/')
def index():
    comment_form = forms.CommentForm()
    title = 'Curso Flask'
    return render_template('index.html', title = title, form = comment_form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# set FLASK_APP=main.py
# set FLASK_ENV=development
# python -m flask run 