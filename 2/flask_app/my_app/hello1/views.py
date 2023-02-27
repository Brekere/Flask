from my_app import app

@app.route('/')
@app.route('/hello1')
def hello1():
    return "hola mundo"