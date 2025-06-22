from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@app.route('/informacion')
def informacion():
    return render_template("informacion.html")

@app.route('/entradas')
def entradas():
    return render_template("entradas.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/deportes')
def deportes():
    return render_template("deportes.html")

@app.route('/entrada-general')
def entrada_general():
    return render_template("entrada-general.html")
@app.route('/inscripcion-equipo')
def inscripcion_equipo():
    return render_template("inscripcion-equipo.html")
if __name__ == '__main__':
    app.run(debug=True)
    