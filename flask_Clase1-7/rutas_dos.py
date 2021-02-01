from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola man! :D Cómo andas?'

# http://127.0.0.1:5000/params/
# http://127.0.0.1:5000/params/Javo
# http://127.0.0.1:5000/params/Javo/3
@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name = 'no name', num = 'no num'):
    return 'El parametro es: {} y {}'.format(name, num)

if __name__ == '__main__':
    app.run()

# set FLASK_APP=rutas_dos.py
# set FLASK_ENV=development
# python -m flask run 
