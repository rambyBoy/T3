from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField, SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registration_form(FlaskForm):
	nombres = StringField('Nombres',
						validators=[DataRequired(),Length(min=2, max=20)])

	apellidos = StringField('Apellidos',
							validators=[DataRequired(),Length(min=2, max=30)])

	email = StringField('Email',validators=[DataRequired(),Email()])

	privilegios =SelectField('Privilegios',
							choices=[
								('1','Nivel I (lectura)'),
								('2','Nivel II (lectura y escritura)'),
								('3','Nivel III (lectura, escritura y edición)'),
								],default=1)

	password = PasswordField('Contraseña',
							validators=[DataRequired(),Length(min=5, max=20)])

	confirm_password = PasswordField('Confirmar contraseña',
									validators=[DataRequired(),
												Length(min=5, max=20),
												EqualTo('password')])

	submit= SubmitField('Registrar')


class login_form(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])

	password = PasswordField('Contraseña',validators=[DataRequired()])
	remember=BooleanField('remember_me')
	submit= SubmitField('Ingresar')

# class query_form(FlaskForm):
# 	query = StringField('Query',validators=[DataRequired()])
# 	tabla = StringField('tabla',validators=[DataRequired()])
# 	submit= SubmitField('Crear')

class vehiculo_form(FlaskForm):
	modelo = StringField('Modelo',
						validators=[DataRequired(),Length(min=2)])

	marca = StringField('Marca',
							validators=[DataRequired(),Length(min=2, max=30)])

	año = IntegerField('Año',validators=[DataRequired()])

	tipo =SelectField('Tipo de Vehiculo',
							choices=[
								('Aviones','Avion'),
								('Carros','Carro'),
								('Motos','Moto'),
								('Autobuses','Autobus')
								],default=1)
	precio = IntegerField('Precio',validators=[DataRequired()])

	submit= SubmitField('Registrar')


class editar_vehiculo_form(FlaskForm):
	modelo = StringField('Modelo',
						validators=[DataRequired(),Length(min=2)])

	marca = StringField('Marca',
							validators=[DataRequired(),Length(min=2, max=30)])

	año = IntegerField('Año',validators=[DataRequired()])

	precio = IntegerField('Precio',validators=[DataRequired()])

	submit= SubmitField('Registrar')