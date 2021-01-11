from flask import Flask, render_template
import json


datos = {
    
    "1": "Python",
    "2": "Java",
    "3": "PHP",
    "4": "JavaScript",
    "5": "C++"
}

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/listar')
def listar():
    sin_codificar = json.dumps(datos)
    return json.loads(sin_codificar)