
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hola! Aplicación de Jenifer :#</h1>
    <p>Esta es mi aplicación para el examen</p>
    <a href="/suma/5/3">Probar suma: 5 + 3</a><br>
    <a href="/resta/10/4">Probar resta: 10 - 4</a>
    '''

@app.route('/suma/<path:a>/<path:b>')
def sumar(a, b):
    a = int(a)
    b = int(b)
    resultado = a + b
    return f'<h2>Resultado de {a} + {b} = {resultado}</h2>'

@app.route('/resta/<path:a>/<path:b>')
def restar(a, b):
    a = int(a)
    b = int(b)
    resultado = a - b
    return f'<h2>Resultado de {a} - {b} = {resultado}</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)