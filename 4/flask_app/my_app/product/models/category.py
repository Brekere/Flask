from my_app import db

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FormField, FieldList
from wtforms.validators import InputRequired, ValidationError
from flask_wtf.file import FileField, FileRequired



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    file = db.Column(db.String(255))
    products = db.relationship('Product', backref='category', lazy='select')

    def __init__(self, name, file):
        self.name = name
        self.file = file

    def __repr__(self):
        return '<Category %r>' % (self.name)


def check_category2(form, field):
    res = Category.query.filter_by(name = field.data).first()
    if res:
        raise ValidationError("La categoria: %s ya fue tomada" % field.data)

def check_category(contain=True):
    def _check_category(form, field):
        if contain:
            res = Category.query.filter(Category.name.like("%"+field.data+"%")).first()
        else:
            res = Category.query.filter(Category.name.like(field.data)).first()

        #Validacion para cuando queremos crear un registro con el mismo nombre
        if res and form.id.data == "":
            raise ValidationError("La categoria: %s ya fue tomada" % field.data)

        #Validacion para actualizar
        if res and form.id.data and res.id != int(form.id.data):
            raise ValidationError("La categoria: %s ya fue tomada" % field.data)
    return _check_category


class PhoneForm(FlaskForm):
    phoneCode = StringField("Codigo del telefono")
    countryCode = StringField("Codigo del pais")
    phone = StringField("Telefono")


class PhoneForm2(FlaskForm):
    phoneCode2 = StringField("Codigo del telefono2")


class CategoryForm(PhoneForm, PhoneForm2):
    name = StringField('Nombre: ', validators=[InputRequired(), check_category()]) #(contain=False)
    file = FileField('Archivo') #,validators=[FileRequired()]
    id = HiddenField('Id')
    phonelist = FormField(PhoneForm)
    phone = FieldList(FormField(PhoneForm))


