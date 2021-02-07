from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

import email_validator

class CommentForm(Form):
    username = StringField('username',
    [
        validators.DataRequired(message='El username es requerido'),
        validators.length(min=4, max=25, message='Ingrese un username de entre 4 y 25 caracteres')
    ])
    email = EmailField('Correo electronico',
    [
        validators.DataRequired(message='El username es requerido'),
        validators.Email(message='Ingrese un mail válido')
    ])
    comment = TextField('Comentario')