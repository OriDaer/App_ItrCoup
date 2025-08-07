from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "clave_secreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/itr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colegio = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    disciplina = db.Column(db.String(20), nullable=True)
    categoria = db.Column(db.String(20), nullable=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10,2), nullable=False)
    imagen = db.Column(db.String(100), nullable=False)


class Inscripcion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    contacto = db.Column(db.String(120), nullable=False)
    nombre_transferencia = db.Column(db.String(120), nullable=False)
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    colegios = ['Instituto Técnico Renault', 'Esclavas', 'Sol de Mayo', 'San Patricio']
    disciplinas = ['voley', 'futbol', 'basquet']
    categorias = ['menor', 'mayor', 'intermedia']
    error = None

    if request.method == 'POST':
        usuario = request.form.get('usuario').strip()
        contraseña = request.form.get('contraseña').strip()
        colegio = request.form.get('colegio')
        rol = request.form.get('rol')
        disciplina = request.form.get('disciplina')
        categoria = request.form.get('categoria')

        # Comenzamos la consulta
        query = Usuario.query.filter_by(usuario=usuario, contraseña=contraseña)

        if colegio:
            query = query.filter_by(colegio=colegio)
        if rol:
            query = query.filter_by(rol=rol)
        if rol == 'jugador':
            if disciplina:
                query = query.filter_by(disciplina=disciplina)
            if categoria:
                query = query.filter_by(categoria=categoria)

        user = query.first()

        if user:
            session['usuario'] = user.usuario
            session['colegio'] = user.colegio
            return redirect(url_for('index'))
        else:
            error = "Datos incorrectos. Verificá todo antes de iniciar sesión."

    return render_template('login.html', colegios=colegios, disciplinas=disciplinas,
                        categorias=categorias, error=error)

@app.route('/index')
def index():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("index.html", usuario=session["usuario"])

@app.route('/nosotros')
def nosotros():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("nosotros.html", usuario=session["usuario"])

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

@app.route('/cantina')
def cantina():
    if "usuario" not in session:
        return redirect("/login")
    productos = Producto.query.all()
    for p in productos:
        print(p.nombre, p.precio, p.imagen)
    return render_template("cantina.html", productos=productos, usuario=session["usuario"])

@app.route('/entrada-general')
def entrada_general():
    if "usuario" not in session:
        return redirect("/login")
    #precio=210.000
    return render_template("entrada-general.html", usuario=session["usuario"])

@app.route('/inscripcion-equipo')
def inscripcion_equipo():
    if "usuario" not in session:
        return redirect("/login")
    deporte = request.args.get('deporte', 'No especificado')
    print("Deporte seleccionado:", deporte) 
    return render_template("inscripcion-equipo.html", usuario=session["usuario"])

@app.route('/inscripcion', methods=['POST'])
def inscripcion():
    if "usuario" not in session:
        return redirect("/login")
    contacto = request.form.get('contacto')
    deporte = request.form.get('deporte')
    return render_template("confirmacion.html", contacto=contacto, deporte=deporte, usuario=session["usuario"])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)