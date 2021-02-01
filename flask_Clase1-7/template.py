from flask import Flask
from flask import render_template

app = Flask(__name__)
# Si cambio el nombre de la carpeta 'templates', debo colocarlo como
#argumento:
# app = Flask(__name__, template_folder = "templatePrueba")

@app.route('/')
def index():
    return render_template('index.html') # Busca el archivo dentro de
                                        # la caperta templates

if __name__ == '__main__':
    app.run()

# set FLASK_APP=template.py
# set FLASK_ENV=development
# python -m flask run 
