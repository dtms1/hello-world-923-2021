from flask import Flask, render_template
from config import db
from controller.usuario import usuario_blueprint

TEMPLATES = "./view"
STATIC = "./static"

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# Definição das Rotas

@app.route('/')
def helloWorld():
    return render_template('login.html')

@app.route('/login', methods={'POST'})
def login():
    return render_template('index.html')

@app.route('/index')
def index():
    nome = 'Flávio'
    mostrarVideos = True
    lista = ['https://www.youtube.com/embed/vU3RHRELdCE', 'https://www.youtube.com/embed/uUUYv_T1dEs', 'https://www.youtube.com/embed/n3tMEOw9KGY']
    return render_template('hello-world.html', nome=nome, lista=lista, mostrarVideos=mostrarVideos)

#app.run(host="0.0.0.0", port=5000)