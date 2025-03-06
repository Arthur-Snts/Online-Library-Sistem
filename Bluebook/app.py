from controllers import Book, User, Lending, listagem
from flask import Flask, render_template

app = Flask(__name__)
app.register_blueprint(Book.bp)
app.register_blueprint(User.bp)
app.register_blueprint(Lending.bp)
app.register_blueprint(listagem.bp)

@app.route('/')
def index():
    return render_template("index.html")


# Todas as rotas

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/book')
def book():
    return render_template("book.html")

@app.route('/dados_livros')
def dados_livros():
    return render_template("dados_livros.html")

@app.route('/editar_livros')
def editar_livros():
    return render_template("editar_livros.html")

@app.route('/editar_emprestimos')
def editar_emprestimos():
    return render_template("editar_emprestimos.html")

@app.route('/dados_usuarios')
def dados_usuarios():
    return render_template("dados_usuarios.html")

@app.route('/dados_emprestimos')
def dados_emprestimos():
    return render_template("dados_emprestimos.html")

@app.route('/editar_usuarios')
def editar_usuarios():
    return render_template("editar_usuarios.html")

@app.route('/lending')
def lending():
    return render_template("lending.html")

@app.route('/listagem_um')
def listagem_um():
    return render_template("listagem_um.html")

@app.route('/listagem_dois')
def listagem_dois():
    return render_template("listagem_dois.html")

@app.route('/listagem_tres')
def listagem_tres():
    return render_template("listagem_tres.html")

@app.route('/listagem_quatro')
def listagem_quatro():
    return render_template("listagem_quatro.html")

@app.route('/pg_listagem')
def pg_listagem():
    return render_template("pg_listagem.html")

@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/logs')
def logs():
    return render_template("logs.html")





