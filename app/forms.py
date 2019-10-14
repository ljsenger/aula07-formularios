from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, 
BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	usuario = StringField(u'Nome de usuário', validators=[DataRequired()])
	senha = PasswordField(u'Senha', validators=[DataRequired()])
	lembre_me = BooleanField(u'Lembre-me')
	submit = SubmitField(u'Entrar')