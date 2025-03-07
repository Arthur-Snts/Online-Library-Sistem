from flask import Blueprint, render_template, request, url_for, redirect
from models.Lending import Lending
from models.Leitor import Leitor
from models.Book import Book
from models.Listagem import Listagem
from flask_login import login_required, current_user

bp = Blueprint("listagem", __name__, url_prefix="/listagem")

@bp.route('/')
@login_required
def listagens():
    user = current_user
    return render_template("pg_listagem.html", user = user)


@bp.route('/filtro1', methods=['GET', 'POST'])
@login_required
def filtro1():
    
    if request.method == 'POST':
        use_id = request.form.get('usuario')
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        total_emprestimos = Listagem.um(use_id, data1, data2)
        consulta_usuarios = Leitor.all()
        user = current_user
        return render_template('listagem_um.html', total_emprestimos=total_emprestimos, consulta_usuarios=consulta_usuarios, user = user)
    else:
        consulta_usuarios = Leitor.all()
        user = current_user
        return render_template('listagem_um.html', consulta_usuarios=consulta_usuarios, user = user)
    
@bp.route('/filtro2', methods=['GET', 'POST'])
@login_required
def filtro2():
    if request.method == 'POST':
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        usuarios = Listagem.dois(data1, data2)
        user = current_user
        return render_template('listagem_dois.html', usuarios=usuarios, user = user)
    user = current_user
    return render_template('listagem_dois.html', user = user)

@bp.route('/filtro3', methods=['GET', 'POST'])
@login_required
def filtro3():
    if request.method == 'POST':
        dias = request.form.get('filtro_dias')
        livros = Listagem.tres(dias)
        user = current_user
        return render_template('listagem_tres.html', livros=livros, user = user)
    user = current_user
    return render_template('listagem_tres.html', user = user)

@bp.route('/filtro4', methods=['GET', 'POST'])
@login_required
def filtro4():
    if request.method == 'POST':
        dias = request.form.get('filtro_dias')
        livros = Listagem.quatro(dias)
        user = current_user
        return render_template('listagem_quatro.html', livros=livros, user = user)
    user = current_user
    return render_template('listagem_quatro.html', user = user)

@bp.route('/logs')
@login_required
def logs():
    user = current_user
    logs = Listagem.logs()
    return render_template("logs.html", user = user, logs=logs)