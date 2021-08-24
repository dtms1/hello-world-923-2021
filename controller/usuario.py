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

@usuario_blueprint.route('/deleteuser/<int:id>')
def deletarUser(id):
    user = Usuario.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@usuario_blueprint.route('/user/<int:id>')
def user(id):
    user = Usuario.query.filter_by(id=id).first()
    return render_template('userform.html', usuario=user)



@usuario_blueprint.route('/alterarUsuario', methods=['POST'])
def alterarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    id = request.form.get('id')

    user = Usuario.query.filter_by(id=id).first()

    user.nome = nome
    user.email = email

    db.session.commit()
    if user:
        return 'Usuario alterado'
        
    return 'Usuario alterado'