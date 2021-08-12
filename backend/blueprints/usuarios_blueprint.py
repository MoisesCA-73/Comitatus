from backend.models.login_model import LoginModel
from flask import Flask, url_for, redirect,g
from flask import Blueprint
from flask import request
from flask import jsonify
from flask.templating import render_template

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.usuarios_model import UsuariosModel

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

model = UsuariosModel()
modelLogin = LoginModel()

class User:
    def __init__(self,cui,contrasenia,nombres,apellidos,escuela,correo,imagen):
        self.cui = cui
        self.contrasenia = contrasenia
        self.nombres = nombres
        self.apellidos = apellidos
        self.escuela = escuela
        self.correo = correo
        self.imagen = imagen

@usuarios_blueprint.route('/usuarios')
def Menu():
    if not g.user:
        return redirect(url_for('login_blueprint.Index'))
    return render_template("menu.html")

@usuarios_blueprint.route('/signup', methods=['GET','POST'])
def SignUp():
    if request.method == 'POST':
        cui = request.form['cui']
        contrasenia = request.form['contrasenia']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['email']

        model.create_usuarios(cui,nombres,apellidos,"Ciencia de la Computacion",correo,"imagen01.png")
        modelLogin.create_usuario(cui,contrasenia)

        return redirect(url_for('login_blueprint.Index'))

    return render_template("singup.html")

@usuarios_blueprint.route('/usuarios/create_usuarios', methods=['POST'])
@cross_origin()
def create_usuarios():
    content = model.create_usuarios(request.json['cui'],request.json['nombres'], request.json['apellidos'], request.json['escuela'], request.json['correo'], request.json['imagen'])   
    return jsonify(content)

@usuarios_blueprint.route('/usuarios/delete_usuarios', methods=['POST'])
@cross_origin()
def delete_usuarios():
    return jsonify(model.delete_usuarios(int(request.json['cui'])))

@usuarios_blueprint.route('/usuarios/get_usuarios', methods=['POST'])
@cross_origin()
def usuarios():
    return jsonify(model.get_usuarios(int(request.json['cui'])))

@usuarios_blueprint.route('/usuarios/get_all_usuarios', methods=['POST'])
@cross_origin()
def all_usuarios():
    return jsonify(model.get_all_usuarios())
