from flask import Flask
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
import forms # forms.py

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario")
    title = 'Curso Flask'
    return render_template('index.html', title = title, form = comment_form)

@app.route('/login', methods = ['GET', 'POST'])
def logi():
    login_form = forms.LoginForm()
    return render_template('login.html', form = login_form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# set FLASK_APP=main.py
# set FLASK_ENV=development
# python -m flask run 