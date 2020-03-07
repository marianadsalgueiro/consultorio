from flask_wtf import FlaskForm

class BaseForm(FlaskForm):
    class Meta:
        locales = ['pt', 'en']
