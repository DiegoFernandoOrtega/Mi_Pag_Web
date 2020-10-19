from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100),nullable=False)  
    email = db.Column(db.String(100),nullable=False, unique=True)  
    password = db.Column(db.String(100),nullable=False) 

def __init__(self, nombres, email, password):
    self.nombres = nombres
    self.email = email
    self.password = password

@app.route("/")
def hello():
    nombre = "Diego"
    return render_template("index.html", nombre=nombre)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/registro")
def registro():
    usuarios = usuario.query.all()
    print (usuarios)
    return render_template("auth/registro.html")

@app.route("/registro", methods =['POST'])
def guardar_usuario():
    nombres =request.form['nombres']
    email = request.form['email']
    password = request.form['password']

    nuevo_usuario = Usuario(nombres, email, password)

    password = hashlib.md5()
    password.update(nuevo_usuario.password.encode('utf-8'))
    nuevo_usuario.password = password.hexdigest()

    db.session.add(nuevo_usuario)
    db.session.commit()

    return "Guardando el usuario"

@app.route("/login")
def login():
    return render_template("auth/login.html")



if __name__ == "__main__":
    app.run(debug=True)




