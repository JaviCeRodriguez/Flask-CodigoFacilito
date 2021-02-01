from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola man! :D Cómo andas?'

# http://127.0.0.1:5000/params?name=Javo&surname=Rodriguez
# http://127.0.0.1:5000/params?name=Javo
@app.route('/params')
def params():
    paramName = request.args.get('name', '???')
    paramSurname = request.args.get('surname', '???')
    return 'Nombre completo: {} {}'.format(paramName, paramSurname)

if __name__ == '__main__':
    app.run()

# set FLASK_APP=rutas.py
# set FLASK_ENV=development
# python -m flask run 
