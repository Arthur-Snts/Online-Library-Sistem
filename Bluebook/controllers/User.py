from flask import Blueprint, render_template, request, url_for, redirect
from models.User import User
from models.Lending import Lending
from database import obter_conexao

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        endereco = request.form['endereco']

        User.cadastro(nome, email, telefone, endereco)

        return redirect(url_for('users.listar_user'))
    users = User.all()
    return render_template('user.html',users = users)


@bp.route('/listar_user', methods=['POST', 'GET'])
def listar_user():
    
    if request.method == 'POST':
        order_by = request.form.get('status')

        users = User.listar(order_by)
        
        
        
        return render_template('user.html', users=users)
    users = User.all()
    return render_template('user.html', users = users)


@bp.route('/dados_users/')
def dados_users():
    users = User.all()
    return render_template("dados_usuarios.html", users=users)

@bp.route('/editar_user/<int:id>', methods=['GET', 'POST'])
def editar_user(id):
    

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        User.update(id, nome, email, telefone, endereco)
        return redirect(url_for('users.listar_user'))
    user = User.one(id)
    return render_template('editar_usuarios.html', user = user)


@bp.route('/apagar_user/<int:id>')
def excluir_user(id):
    lendings = Lending.listar("")
    for lending in lendings:
        if id == lending['len_use_id']:
            mensagem = "Possui um empréstimo com esse Usuário, Impossível Excluir"
            users = User.all()
            return render_template("dados_usuarios.html", users = users, mensagem = mensagem)
    User.delete(id)
    return redirect(url_for('users.listar_user'))