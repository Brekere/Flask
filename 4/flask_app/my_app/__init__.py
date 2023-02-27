from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user
from functools import wraps

app = Flask(__name__)

app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "fauth.login"


def rol_admin_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.rol.value != 'Administrador':
            logout_user()
            return redirect(url_for('fauth.login'))
            # login_manager.unauthorized()
            # return "Tu debes de ser administrador",403
            # print('Llamando a la funcion del decorador '+str(current_user.rol.value))
        return f(*args, **kwds)
    return wrapper

from my_app.product.product import product
from my_app.fauth.views import fauth
from my_app.auth.views import auth
from my_app.product.category import category

# importar las vistas
app.register_blueprint(product)
app.register_blueprint(category)
# app.register_blueprint(auth)
app.register_blueprint(fauth)

with app.app_context():
    db.create_all()


@app.template_filter('myDouble')
def myDouble_filter(n):
    return n*2

