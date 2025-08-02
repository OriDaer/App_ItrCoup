from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "clave_secreta"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/itr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de tabla
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)

@app.route("/")
def index():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("index.html", usuario=session["usuario"])
    
@app.route("/login")
def login():
    if "usuario" in session:
        return redirect("/")
    return render_template("login.html")

@app.route("/iniciar_sesion", methods=["POST"])
def iniciar_sesion():
    usuario = request.form.get("usuario", "")
    contraseña = request.form.get("contraseña", "")
    user = Usuario.query.filter_by(usuario=usuario, contraseña=contraseña).first()
    if user:
        session["usuario"] = user.usuario
        return redirect("/")
    else:
        return render_template("login.html", error="Usuario o contraseña incorrectos")

@app.route('/nosotros')
def nosotros():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("nosotros.html" , usuario=session["usuario"])

@app.route('/informacion')
def informacion():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("informacion.html", usuario=session["usuario"])

@app.route('/entradas')
def entradas():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("entradas.html", usuario=session["usuario"])

@app.route('/deportes')
def deportes():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("deportes.html", usuario=session["usuario"])

@app.route('/entrada-general')
def entrada_general():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("entrada-general.html", usuario=session["usuario"])

@app.route('/inscripcion-equipo')
def inscripcion_equipo():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("inscripcion-equipo.html", usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)
