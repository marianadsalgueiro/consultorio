from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from .base_form import BaseForm
 
class ContactForm(BaseForm):
  nome = StringField(validators=[DataRequired("Por favor, preencha este campo.")])
  email = StringField(validators=[DataRequired("Por favor, preencha este campo."), Email("Email inválido")])
  mensagem = TextAreaField(validators=[DataRequired("Por favor, preencha este campo.")])
  submit = SubmitField("Enviar")