from flask import Blueprint, render_template, request, url_for, redirect
from models.Lending import Lending
from models.Leitor import Leitor
from models.Book import Book
from database import obter_conexao
from flask_login import login_required, current_user
import ast

bp = Blueprint("lendings", __name__, url_prefix="/lendings")



@bp.route('/register_emprestimo', methods=['GET', 'POST'])
@login_required
def register_lending():
    if request.method == 'POST':
        usuario = request.form["usuario"]
        livro = request.form["livro"]
        devolucao = request.form["devolucao"]
        valor = request.form["valor"]
        user = current_user.id
        mensagem = Lending.cadastro(usuario=usuario, livro=livro, devolucao=devolucao, valor=valor, user = user)
        return redirect(url_for("lendings.listar_lending", mensagem=mensagem))

    else:
        consulta_leitores = Leitor.all()
        consulta_livros = Book.all()
        emprestimos = Lending.listar("")
        user = current_user
        return render_template('lending.html', consulta_livros=consulta_livros, consulta_leitores=consulta_leitores,emprestimos = emprestimos, user = user)
   

@bp.route('/listar_emprestimo', methods=['GET', 'POST'])
@login_required
def listar_lending():
    if request.method == 'POST':
        order_by = request.form.get('listar_emprestimos')

        emprestimos = Lending.listar(order_by)
        
        consulta_usuarios = Leitor.all()
        consulta_livros = Book.all()
        user = current_user
        if mensagem in request.args:
            mensagem = request.args.get("mensagem")
        return render_template('lending.html', emprestimos=emprestimos, consulta_livros=consulta_livros, consulta_usuarios=consulta_usuarios, user = user, mensagem=mensagem)
    emprestimos = Lending.listar("")
    consulta_usuarios = Leitor.all()
    consulta_livros = Book.all()
    user = current_user
    
    if "mensagem" in request.args:
            mensagem = request.args.get("mensagem")
            try:
                mensagem_dict = ast.literal_eval(mensagem)  # Converte string para dicionário real
                if isinstance(mensagem_dict, dict) and "@mensagem" in mensagem_dict:
                    mensagem = mensagem_dict["@mensagem"]  # Pega apenas o texto dentro do dicionário
            except (SyntaxError, ValueError):
                pass
    return render_template('lending.html', emprestimos=emprestimos , consulta_livros=consulta_livros, consulta_leitores=consulta_usuarios, user = user, mensagem= mensagem )

@bp.route('/dados_emprestimos/')
@login_required
def dados_emprestimos():
    emprestimos = Lending.all()
    user = current_user
    return render_template("dados_emprestimos.html", emprestimos = emprestimos, user = user)



@bp.route('/editar_empréstimo/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_lending(id):
    

    if request.method == 'POST':
        leitor = request.form["leitor"]
        livro = request.form["livro"]
        valor = request.form["valor"]
        devolucao = request.form["data"]
        print(leitor,livro,valor,devolucao)
        Lending.update(leitor,livro, devolucao, valor,current_user.id, id)
        return redirect(url_for('lendings.dados_emprestimos'))
    
    lending = Lending.one(id)
    leitores = Leitor.all()
    books = Book.all()
    user = current_user
    return render_template('editar_emprestimos.html', emp=lending, user = user, leitores=leitores, books=books)


@bp.route('/apagar_empréstimo/<int:id>')
@login_required
def excluir_lending(id):
    Lending.delete(id)
    return redirect(url_for('lendings.dados_emprestimos'))

@bp.route('/devolver/<int:id>')
@login_required
def devolver(id):
    conn = obter_conexao()
    cursor = conn.cursor()
    query = 'UPDATE tb_lending SET len_devolvido =%s WHERE len_id = %s'
    cursor.execute(query, (True, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("lendings.dados_emprestimos"))




