from flask_login import UserMixin
from proyecto import login_manager

class user(UserMixin):
	"""docstring for user"""
	def __init__(self,id, nombre, apellido, contraseña, correo, privilegios):

		self.id = id
		self.nombre= nombre
		self.apellido=apellido
		self.correo=correo
		self.contraseña=contraseña
		self.privilegios=privilegios