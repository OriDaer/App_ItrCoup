from flask import Flask, render_template, redirect, url_for

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

if __name__ == '__main__':
    app.run(debug=True)
    