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

