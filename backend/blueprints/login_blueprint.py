from backend.models.usuarios_model import UsuariosModel
from flask import (Flask, render_template,url_for,g,session)
from flask import Blueprint
from flask import request
from flask import jsonify
from flask.helpers import url_for
from flask.templating import render_template_string

from flask_cors import CORS, cross_origin
from werkzeug.utils import redirect # para que no genere errores de CORS al hacer peticiones

from backend.models.login_model import LoginModel

login_blueprint = Blueprint('login_blueprint', __name__,)

model = LoginModel()
modelUser = UsuariosModel()

class User:
    def __init__(self,id, cui, contrasenia, nombres, apellidos, escuela, correo, imagen):
        self.id = id
        self.cui = cui
        self.contrasenia = contrasenia
        self.nombres = nombres
        self.apellidos = apellidos
        self.escuela = escuela
        self.correo = correo
        self.imagen = imagen
    def __repr__(self):
        return f'<User:  {self.cui}>'

users = []
list_log = model.get_all_usuario()
list_user = modelUser.get_all_usuarios()


n = 1
for x, y in zip(list_log,list_user):
    users.append(User(id=n, cui=x.get('cui'), contrasenia=x.get('contrasenia'),nombres=y.get('nombres'),apellidos=y.get('apellidos'),escuela=y.get('escuela'),correo=y.get('correo'),imagen=y.get('imagen')))
    n += 1


@login_blueprint.before_app_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@login_blueprint.route('/login', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        session.pop('user_id', None)
        cui = request.form['cui']
        contrasenia = request.form['contrasenia']
        
        user = [x for x in users if x.cui == cui][0]

        if user and user.contrasenia== contrasenia:
            session['user_id'] = user.id
            return redirect(url_for('usuarios_blueprint.Menu'))

        return redirect(url_for('login_blueprint.Index'))
    return render_template('login.html')

@login_blueprint.route('/login/create_usuario', methods=['POST'])#Verificar si se encuentra en la base de datos
@cross_origin()
def create_usuario():
    content = model.create_usuario(int(request.form['cui']), request.form['contrasenia'])    
    return content

@login_blueprint.route('/login/delete_usuario', methods=['POST'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['cui'])))

@login_blueprint.route('/login/get_usuario', methods=['POST'])
@cross_origin()
def usuario():
    return jsonify(model.get_usuario(int(request.json['cui'])))

@login_blueprint.route('/login/get_all_usuario', methods=['POST'])
@cross_origin()
def all_usuarios():
    return jsonify(model.get_all_usuario())