from flask import Blueprint, render_template, request, url_for, redirect
from models.Book import Book
from models.Lending import Lending
from database import obter_conexao

bp = Blueprint("books", __name__, url_prefix="/books")


@bp.route('/register_book', methods=['GET', 'POST'])
def register_book():
    if request.method == 'POST':
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        genero = request.form["genero"]
        quant_estoque = request.form["estoque"]
        isbn = request.form["isbn"]

        Book.cadastro(titulo, autor, genero, isbn, quant_estoque)
        return redirect(url_for('books.listar_book'))
    
    books= Book.listar(order_by='')
    return render_template('book.html', books=books)

@bp.route('/listar_book', methods=['GET', 'POST'])
def listar_book():

    books= Book.listar(order_by='asc')
    if request.method == 'POST':
        order_by = request.form['status']

        
        books = Book.listar(order_by=order_by)
    
    return render_template('book.html', books = books)

@bp.route('/dados_livro')
def dados_livros():
    books = Book.all()
    return render_template("dados_livros.html", books=books)


@bp.route('/editar_book/<int:id>', methods=['GET', 'POST'])
def editar_book(id):
    

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        genero = request.form.get('genero')
        isbn = request.form.get('isbn')
        estoque = request.form.get('estoque')
        Book.update(id,titulo, autor, genero, isbn, estoque)
        return redirect(url_for('books.listar_book'))
    book = Book.one(id)
    return render_template('editar_livros.html', book = book)


@bp.route('/apagar_book/<int:id>')
def excluir_book(id):
    lendings = Lending.listar("")
    for lending in lendings:
        if id == lending['len_boo_id']:
            mensagem = "Esse Livro está sendo emprestado, Impossível Excluir"
            books = Book.all()
            return render_template("dados_livros.html", books=books, mensagem = mensagem)
    Book.delete(id)
    return redirect(url_for('books.listar_book'))