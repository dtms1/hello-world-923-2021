from flask import render_template, request, Blueprint
from config import db
from model.usuario import Usuario

TEMPLATES = "./view"
STATIC = "./static"

usuario_blueprint = Blueprint('usuarios', __name__, template_folder=TEMPLATES, static_folder=STATIC)

@usuario_blueprint.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')

    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email:
            return 'Email já cadastrado!'

    usuario = Usuario(nome, email)
    db.session.add(usuario)
    db.session.commit()
    return 'Usuário cadastrado com sucesso!'

@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@usuario_blueprint.route('/usuarios/form')
def abrirCadastroUsuario():
    return render_template('cadastrarUsuario.html')

@app.route("/usuario/<id>" , methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso.")
    except Exception as e:
        print("Erro", e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")

@app.route("/usuario/<id>", methods= ["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao deletar")
