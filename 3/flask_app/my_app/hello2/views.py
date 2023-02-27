#from my_app import app
from flask import Blueprint

hello2=Blueprint('Hello2',__name__)

@hello2.route('/')
@hello2.route('/hello2')
def shello():
    return "hola mundo hello2"