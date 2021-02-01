from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='Javo'):
    age = 25
    my_list = [1, 2, 3, 7]
    return render_template('user.html', nombre=name, edad=age, lista=my_list)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)

    
# set FLASK_APP=variables.py
# set FLASK_ENV=development
# python -m flask run 