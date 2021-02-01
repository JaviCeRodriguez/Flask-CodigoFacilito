from flask import Flask

app = Flask(__name__) # Objeto creado

@app.route('/') # Wrap o decorador
def index():
    return 'Hola mundo' # Regresa un string

app.run() # Se encarga de ejecutar el servidor