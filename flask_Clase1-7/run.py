from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola man! :D Cómo andas?'

if __name__ == '__main__':
    app.run(debug = True, port = 8000)

# set FLASK_APP=run.py
# set FLASK_ENV=development
# python -m flask run 
