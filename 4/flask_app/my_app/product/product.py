# from my_app import app
import os
from my_app import db, app, ALLOWED_EXTENSIONS_FILE
from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from werkzeug.utils import secure_filename
from flask_login import login_required
from sqlalchemy.sql.expression import not_, or_

from my_app.product.models.products import PRODUCTS
from my_app.product.models.product import Product
from my_app.product.models.category import Category

from my_app.product.models.product import ProductForm
from my_app import rol_admin_need

product = Blueprint('product', __name__)

@product.before_request
@login_required
@rol_admin_need
def constructor():
    pass

def allowed_extensions_file(filename):
    return '.' in filename and filename.lower().rsplit('.',1)[1] in ALLOWED_EXTENSIONS_FILE


@product.route('/product')
@product.route('/products/<int:page>')
def index(page=1):
    return render_template('product/index.html', products=Product.query.paginate(page=page, per_page=5))


#@product.route('/product', default = {'id':1}) esto solo es una cofiguracion de url para default no aplicable en este ejemplo
@product.route('/product/<int:id>')
def show(id):
    product = Product.query.get_or_404(id)
    return render_template('product/show.html', product=product)


@product.route('/product-create', methods=('GET', 'POST'))
def create():
    form = ProductForm() #meta={'csrf': False}

    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category_id.choices = categories

    if form.validate_on_submit():
        # Crear un registro
        p = Product(request.form['name'], request.form['price'], request.form['category_id'], request.form['file'])
        db.session.add(p)
        db.session.commit()
        flash("Producto creado con exito")
        return redirect(url_for('product.create'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('product/create.html', form=form)


@product.route('/product-update/<int:id>', methods=['GET', 'POST'])
def update(id):
    product = Product.query.get_or_404(id)
    form = ProductForm() #meta={'csrf': False}

    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category_id.choices = categories

    if request.method == 'GET':
        form.name.data = product.name
        form.price.data = product.price
        form.category_id.data = product.category_id

    if form.validate_on_submit():
        # actualizar un registro
        product.name = form.name.data
        product.price = form.price.data
        product.category_id = form.category_id.data

        if form.file.data:
         file = form.file.data
         if allowed_extensions_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            product.file = filename

        db.session.add(product)
        db.session.commit()
        flash("Producto actualizado con exito")
        return redirect(url_for('product.update', id=product.id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('product/update.html', product=product, form=form)


@product.route('/product-delete/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()
    flash("Producto borrado con exito")

    return redirect(url_for('product.index'))


@product.route('/test')
def test():
    # p = Product.query.all()#imprimir todos los registros
    # p = Product.query.limit(2).all()#es para imprimir cierto numero de registros
    # p = Product.query.first()  # este es para imprimir el primer registro
    # p = Product.query.order_by(Product.id.desc())#es para ordenarlos
    # p = Product.query.get({"id:1"})# es para buscar por un atributo en especifico solo funciona para seguirity key
    # p = Product.query.filter_by(name="p1").all()# este es ´para buscar un atributo es especifico
    # p = Product.query.filter(Product.name.like('P%')).all()#es para buscar en los registros los que tengan algo escrito despues de la letra P
    # p = Product.query.filter(not_(Product.id>1)).all()#este es para negar
    # p = Product.query.filter(or_(Product.id>1,Product.name=="P1")).all()
    # print(p)
    '''#Crear un registro
    p=Product("P5",60.8)
    db.session.add(p)
    db.session.commit()'''

    '''#actualizar
    p = Product.query.filter_by(name="P1").first()
    p.name="UP1"
    db.session.add(p)
    db.session.commit()'''

    '''#eliminar
    p = Product.query.filter_by(id=1).first()
    db.session.delete(p)
    db.session.commit()'''

    return "Flask"


@product.route('/filter/<int:id>')
def filter(id):
    product = PRODUCTS.get(id)
    return render_template('product/filter.html', product=product)


@product.app_template_filter('iva')
def iva_filter(product):
    if product["price"]:
        return (product["price"]*1.20)
    return "Sin precio"
