from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from models.User import User

bp = Blueprint(url_prefix="/users", name="users", import_name=__name__)

@bp.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        users = User.all()
        for usuario in users:
            print(usuario[1])
            if nome in usuario[1]:
                user = User.nome(nome=nome)
                if user.senha == senha:
                    login_user(user)
                    return redirect(url_for("index"))
        return redirect(url_for("users.login"))
    else:
        return render_template("login.html")
        

@bp.route('/cadastro', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        tipo = request.form["tipo"]
        User.insert(nome=nome, tipo=tipo, senha=senha)
        return redirect(url_for("index"))
    else:
        user = current_user
        return render_template("cadastro.html", user = user)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))