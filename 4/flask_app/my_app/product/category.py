# from my_app import app
from my_app import db, rol_admin_need
from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages

from my_app.product.models.category import Category
from sqlalchemy.sql.expression import not_, or_
from my_app.product.models.category import CategoryForm
from flask_login import login_required

category = Blueprint('category', __name__)


@category.before_request
@login_required
@rol_admin_need
def constructor():
    pass


@category.route('/category')
@category.route('/categories/<int:page>')
def index(page=1):
    return render_template('category/index.html', categories=Category.query.paginate(page=page, per_page=5))


@category.route('/category/<int:id>')
def show(id):
    category = Category.query.get_or_404(id)
    return render_template('category/show.html', category=category)


@category.route('/category-create', methods=('GET', 'POST'))
def create():
    form = CategoryForm(meta={'csrf': False})
    if form.validate_on_submit():
        # Crear un registro
        p = Category(request.form['name'])
        db.session.add(p)
        db.session.commit()
        flash("Categoria creada con exito")
        return redirect(url_for('category.create'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('category/create.html', form=form)


@category.route('/category-update/<int:id>', methods=['GET', 'POST'])
def update(id):
    category = Category.query.get_or_404(id)
    form = CategoryForm(meta={'csrf': False})

    if request.method == 'GET':
        form.name.data = category.name

    if form.validate_on_submit():
        # actualizar un registro
        category.name = form.name.data

        db.session.add(category)
        db.session.commit()
        flash("Categoria actualizada con exito")
        return redirect(url_for('category.update', id=category.id))

        if form.errors:
            flash(form.errors, 'danger')

    return render_template('category/update.html', category=category, form=form)


@category.route('/category-delete/<int:id>')
def delete(id):
    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()
    flash("Categoria borrada con exito")

    return redirect(url_for('category.index'))


@category.route('/test')
def test():
    # p = Category.query.all()#imprimir todos los registros
    # p = Category.query.limit(2).all()#es para imprimir cierto numero de registros
    # p = Category.query.first()  # este es para imprimir el primer registro
    # p = Category.query.order_by(Category.id.desc())#es para ordenarlos
    # p = Category.query.get({"id:1"})# es para buscar por un atributo en especifico solo funciona para seguirity key
    # p = Category.query.filter_by(name="p1").all()# este es ´para buscar un atributo es especifico
    # p = Category.query.filter(Category.name.like('P%')).all()#es para buscar en los registros los que tengan algo escrito despues de la letra P
    # p = Category.query.filter(not_(Category.id>1)).all()#este es para negar
    # p = Category.query.filter(or_(Category.id>1,Category.name=="P1")).all()
    # print(p)
    '''#Crear un registro
    p=Category("P5",60.8)
    db.session.add(p)
    db.session.commit()'''

    '''#actualizar
    p = Category.query.filter_by(name="P1").first()
    p.name="UP1"
    db.session.add(p)
    db.session.commit()'''

    '''#eliminar
    p = Category.query.filter_by(id=1).first()
    db.session.delete(p)
    db.session.commit()'''

    return "Flask"


@category.app_template_filter('iva')
def iva_filter(category):
    if category["price"]:
        return (category["price"]*1.20)
    return "Sin precio"
