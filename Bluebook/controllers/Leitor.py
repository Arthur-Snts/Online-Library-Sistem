from flask import Blueprint, render_template, request, url_for, redirect
from models.Leitor import Leitor
from models.Lending import Lending
from database import obter_conexao
from flask_login import login_required, current_user

bp = Blueprint("leitores", __name__, url_prefix="/leitores")


@bp.route('/register_leitor', methods=['POST', 'GET'])
@login_required
def register_leitor():
    if request.method == 'POST':
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        endereco = request.form['endereco']

        Leitor.cadastro(nome, email, telefone, endereco)

        return redirect(url_for('leitores.listar_leitor'))
    leitores = Leitor.all()
    user = current_user
    return render_template('leitor.html',leitores = leitores, user = user)


@bp.route('/listar_leitor', methods=['POST', 'GET'])
@login_required
def listar_leitor():
    
    if request.method == 'POST':
        order_by = request.form.get('status')

        leitores = Leitor.listar(order_by)
        
        
        user = current_user
        return render_template('leitor.html', leitores=leitores, user = user)
    leitores = Leitor.all()
    user = current_user
    return render_template('leitor.html', leitores = leitores, user = user)


@bp.route('/dados_leitores/')
@login_required
def dados_leitores():
    leitores = Leitor.all()
    user = current_user
    return render_template("dados_leitores.html", leitores=leitores, user = user)

@bp.route('/editar_leitor/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_leitor(id):
    

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        Leitor.update(id, nome, email, telefone, endereco)
        return redirect(url_for('leitores.listar_leitor'))
    leitor = Leitor.one(id)
    user = current_user
    return render_template('editar_leitores.html', leitor = leitor, user = user)


@bp.route('/apagar_leitor/<int:id>')
@login_required
def excluir_leitor(id):
    lendings = Lending.listar("")
    for lending in lendings:
        if id == lending['len_lei_id']:
            mensagem = "Possui um empréstimo com esse Usuário, Impossível Excluir"
            leitores = Leitor.all()
            user = current_user
            return render_template("dados_leitores.html", leitores = leitores, mensagem = mensagem, user=user)
    Leitor.delete(id)
    return redirect(url_for('leitores.listar_leitor'))