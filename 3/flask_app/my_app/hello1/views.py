#from my_app import app
from flask import Blueprint

hello1=Blueprint('Hello1',__name__)

@hello1.route('/')
@hello1.route('/hello1')
def hello():
    return "hola mundo 1"