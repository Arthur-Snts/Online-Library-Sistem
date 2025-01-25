from flask import Blueprint, render_template, request, url_for, redirect
from models.Lending import Lending
from models.User import User
from models.Book import Book
from models.Listagem import Listagem

bp = Blueprint("listagem", __name__, url_prefix="/listagem")

@bp.route('/')
def listagens():
    return render_template("pg_listagem.html")


@bp.route('/filtro1', methods=['GET', 'POST'])
def filtro1():
    
    if request.method == 'POST':
        use_id = request.form.get('usuario')
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        total_emprestimos = Listagem.um(use_id, data1, data2)
        consulta_usuarios = User.all()
        return render_template('listagem_um.html', total_emprestimos=total_emprestimos, consulta_usuarios=consulta_usuarios)
    else:
        consulta_usuarios = User.all()
    return render_template('listagem_um.html', consulta_usuarios=consulta_usuarios)
    
@bp.route('/filtro2', methods=['GET', 'POST'])
def filtro2():
    if request.method == 'POST':
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        usuarios = Listagem.dois(data1, data2)
        return render_template('listagem_dois.html', usuarios=usuarios)
    return render_template('listagem_dois.html')


@bp.route('/filtro3', methods=['GET', 'POST'])
def filtro3():
    if request.method == 'POST':
        dias = request.form.get('filtro_dias')
        livros = Listagem.tres(dias)
        return render_template('listagem_tres.html', livros=livros)
    return render_template('listagem_tres.html')

@bp.route('/filtro4', methods=['GET', 'POST'])
def filtro4():
    if request.method == 'POST':
        dias = request.form.get('filtro_dias')
        livros = Listagem.quatro(dias)
        return render_template('listagem_quatro.html', livros=livros)
    return render_template('listagem_quatro.html')