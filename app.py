from flask import Flask, render_template

TEMPLATES = "./templates"
STATIC = "./static"

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloWorld():
    return 'Hello World!'

@app.route('/index')
def index():
    nome = 'Flávio'
    mostrarVideos = True
    lista = ['https://www.youtube.com/embed/vU3RHRELdCE', 'https://www.youtube.com/embed/uUUYv_T1dEs', 'https://www.youtube.com/embed/n3tMEOw9KGY']
    return render_template('index.html', nome=nome, lista=lista, mostrarVideos=mostrarVideos)

#app.run(host="0.0.0.0", port=5000)