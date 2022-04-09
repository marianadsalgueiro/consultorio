from flask import render_template, flash
from .forms import ContactForm
from flask_mail import Message, Mail
import os, sys

from app import app

@app.route('/', methods=['GET','POST'])
def index():

	contact_form = ContactForm()

	if contact_form.validate_on_submit():
		msg = Message("[SITE]", sender=os.getenv('EMAIL_USER'), recipients=['{}'.format(os.getenv('EMAIL_USER'))])
		msg.body = """
		From: %s <%s> \n
		%s
		""" % (contact_form.nome.data, contact_form.email.data, contact_form.mensagem.data)
		try:
			print(msg)
			Mail().send(msg)
		except Exception as e:
			print(e)

			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)

			flash('Desculpe, houve um problema com a sua mensagem. Por favor, tente nos contatar diretamente pelo email {}. Obrigado.'.format(os.getenv('EMAIL_USER')), 'danger')
		return render_template('index.html', form=contact_form, mail=os.getenv('EMAIL_USER'))

	return render_template("index.html", form=contact_form, mail=os.getenv('EMAIL_USER'))