from controllers import Book, Lending, listagem, Leitor, User
from flask import Flask, render_template
from flask_login import LoginManager, user_logged_in, current_user
from models.User import User as User_class

app = Flask(__name__)
app.config['SECRET_KEY'] = "superdificil2"
login_manager = LoginManager()
login_manager.init_app(app)
app.register_blueprint(Book.bp)
app.register_blueprint(Leitor.bp)
app.register_blueprint(Lending.bp)
app.register_blueprint(listagem.bp)
app.register_blueprint(User.bp)

login_manager.login_view = "users.login"
login_manager.login_message = "Você precisa fazer login para acessar esta página."
login_manager.login_message_category = "warning" 

@login_manager.user_loader
def load_user(user_id):
    return User_class.get(user_id)



@app.route('/')
def index():
    if user_logged_in:
        user = current_user
    else:
        user = None
    return render_template("index.html", user = user)


# Todas as rotas






