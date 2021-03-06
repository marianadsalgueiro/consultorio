from flask import render_template, flash
from .forms import ContactForm
from flask_mail import Message, Mail

from app import app

@app.route('/', methods=['GET','POST'])
def index():

	contact_form = ContactForm()

	if contact_form.validate_on_submit():
		msg = Message("[SITE RESPONDER]", sender='dramarianaboni@gmail.com', recipients=['dramarianaboni@gmail.com'])
		msg.body = """
		From: %s <%s> \n
		%s
		""" % (contact_form.nome.data, contact_form.email.data, contact_form.mensagem.data)
		try:
			Mail().send(msg)
		except Exception as e:
			print("ENTREI")
			flash('Desculpe, houve um problema com a sua mensagem. Por favor, tente nos contatar diretamente pelo email dramarianaboni@gmail.com. Obrigado.', 'danger')
		return render_template('index.html', form=contact_form)

	return render_template("index.html", form=contact_form)