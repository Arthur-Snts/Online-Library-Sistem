from flask import Blueprint, render_template, request, url_for, redirect
from models.Lending import Lending
from models.User import User
from models.Book import Book
from database import obter_conexao

bp = Blueprint("lendings", __name__, url_prefix="/lendings")



@bp.route('/register_emprestimo', methods=['GET', 'POST'])
def register_emprestimo():
    

    if request.method == 'POST':
        usuario = request.form["usuario"]
        livro = request.form["livro"]
        devolucao = request.form["devolucao"]
        valor = request.form["valor"]

        Lending.cadastro(usuario=usuario, livro=livro, devolucao=devolucao, valor=valor)

        return redirect(url_for("lendings.listar_emprestimo"))

    else:
        consulta_usuarios = User.all()
        consulta_livros = Book.all()
        emprestimos = Lending.listar("")
        return render_template('lending.html', consulta_livros=consulta_livros, consulta_usuarios=consulta_usuarios,emprestimos = emprestimos)
   

@bp.route('/listar_emprestimo', methods=['GET', 'POST'])
def listar_emprestimo():
    if request.method == 'POST':
        order_by = request.form.get('listar_emprestimos')

        emprestimos = Lending.listar(order_by)
        
        consulta_usuarios = User.all()
        consulta_livros = Book.all()
        return render_template('lending.html', emprestimos=emprestimos, consulta_livros=consulta_livros, consulta_usuarios=consulta_usuarios)
    emprestimos = Lending.listar("")
    consulta_usuarios = User.all()
    consulta_livros = Book.all()
    return render_template('lending.html', emprestimos=emprestimos , consulta_livros=consulta_livros, consulta_usuarios=consulta_usuarios )

@bp.route('/dados_emprestimos/<int:id>')
def dados_emprestimos(id):
    return "fazer essa parte"




