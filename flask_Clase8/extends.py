from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Javo'
    return render_template('index.html', name=name)

@app.route('/client')
def client():
    listName = ['Test1', 'Test2', 'Test3']
    return render_template('client.html', list=listName)

if __name__ == '__main__':
    app.run(debug = True)

# set FLASK_APP=extends.py
# set FLASK_ENV=development
# python -m flask run 
