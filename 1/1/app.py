from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/hola')
def hello_world():
    return 'Hola mundo Flask'+__name__


@app.route('/test')
def hello_world2():
    return 'Hola mundo Flask test'


@app.route('/saludar')
@app.route('/saludar/<hi>')
@app.route('/saludar/<hi>/<lang>')
def saludar(hi='persona', lang='es'):
    return 'Hola '+hi+' '+lang

# siempre cambiar pass por return


@app.route('/primer_html')
@app.route('/primer_html/<name>')
def primer_html(name='persona'):
    return '''
        <html>
            <body>
                <hi>hola html</hi>
                <p>hola %s</p>
                <ul>
                    <li>item 1</li>
                    <li>item 2</li>
                </ul>
            </body>
        </html>
    ''' % name


@app.route('/static_file')
def static_file():
    # return "<img src='/static/img/flask.png'>"
    return "<img src="+url_for("static", filename="img/flask.png")+"'>"


@app.route('/mi_primer_template')
@app.route('/mi_primer_template/<name>')
def mi_primer_template(name="persona"):
    return render_template('view.html', name=name)


if __name__ == '__main__':
    app.run()

    '''esto siempre se realiza cuando se esta desarrollando en flask
    para correr los programas desde terminal usando los metods de flask es
    set FLASK_APP=nombre de la app.py
    set FLASK_ENV=developmen (modo desarrollador)
    flask run --reload(importante guardar el programa para despues recargar)'''
