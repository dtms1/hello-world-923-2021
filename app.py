from flask import Flask, render_template, request
from config import db
from usuario import Usuario

TEMPLATES = "./templates"
STATIC = "./static"

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# Definição das Rotas

@app.route('/')
def helloWorld():
    return render_template('cadastroUsuario.html')

@app.route('/index')
def index():
    nome = 'Flávio'
    mostrarVideos = True
    lista = ['https://www.youtube.com/embed/vU3RHRELdCE', 'https://www.youtube.com/embed/uUUYv_T1dEs', 'https://www.youtube.com/embed/n3tMEOw9KGY']
    return render_template('index.html', nome=nome, lista=lista, mostrarVideos=mostrarVideos)

@app.route('/cadastrarUsuario', methods=['POST'])
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

@app.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)

#app.run(host="0.0.0.0", port=5000)