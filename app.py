from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.usuarios_blueprint import usuarios_blueprint
from backend.blueprints.login_blueprint import login_blueprint
from backend.blueprints.curso_del_estudiante_blueprint import curso_del_estudiante_blueprint
from backend.blueprints.escuela_blueprint import escuela_blueprint

app = Flask(__name__)

app.register_blueprint(usuarios_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(curso_del_estudiante_blueprint)
app.register_blueprint(escuela_blueprint)


cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
