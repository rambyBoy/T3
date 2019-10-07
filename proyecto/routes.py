from flask import Flask, render_template, url_for,flash, redirect,request
from proyecto.forms import registration_form, login_form,vehiculo_form, editar_vehiculo_form
from proyecto.conection import conexion, user
from proyecto import app, bcrypt
from proyecto.users import user
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/login',methods=['GET','POST'])
def login():

    form=login_form()

    if form.validate_on_submit():

        conn=conexion()   
        where="email='"+form.email.data+"'"
        #Se crea el objeto usuario y se almacena en la variable usuario
        usuario=conn.select("*","usuarios",where,"1")
        #Se comprueba que las contraseñas coincidan
   
        if bcrypt.check_password_hash(usuario.contraseña,form.password.data):
        	login_user(usuario)
        	return redirect(url_for('opciones'))      	
        else:
        	flash('Email o contraseña Incorrectos, Verifica', 'danger')

    return render_template('index.html', form=form)


@app.route('/registro',methods=['GET','POST'])
@login_required
def registro():

	form = registration_form()

	if form.validate_on_submit():

		nombres=form.nombres.data
		apellidos=form.apellidos.data
		email=form.email.data
		privilegios=form.privilegios.data
		h_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		conn=conexion()
		conn = conn.insert_usuarios(nombres,apellidos, h_password, email, privilegios)
		#Alert diciendo que el usuario se creo correctamente
		return redirect(url_for('opciones'))

	return render_template('crear_usuario.html', form=form)

@app.route('/crear_vehiculo',methods=['GET','POST'])
@login_required
def crear_vehiculo():

	form = vehiculo_form()
	if form.validate_on_submit():

		modelo=form.modelo.data
		marca=form.marca.data
		año=str(form.año.data)
		tipo_vehiculo=form.tipo.data
		precio=str(form.precio.data)

		conn=conexion()
		conn = conn.insert_vehiculos(tipo_vehiculo,modelo, marca, año, 	precio)
		#Alert diciendo que el usuario se creo correctamente
		return redirect(url_for('opciones'))

	return render_template('crear_vehiculo.html', form=form, title="Crear")


@app.route('/usuarios')
@login_required
def usuarios():
	conn=conexion()
	form=conn.select('*',"usuarios","1","2")
	return render_template('usuarios.html',form =form)

@app.route('/opciones')
@login_required
def opciones():
	#query = = """select column_name from information_schema.columns where table_name = 'motos' """
	conn=conexion()
	form=conn.select('*','categoria',"1","2")
	return render_template('opciones.html',form=form,title='Vehículos')

@app.route('/ver/<opcion>')
@login_required
def ver(opcion):
	conn=conexion()
	form=conn.select('*',opcion,"1","2")
	return render_template('ver.html',form=form,title=opcion)

@app.route("/logout")
def logout():
    logout_user()
    print("SESION CERRADA")
    return redirect(url_for('login'))

"""
@app.route("/creartabla")
@login_required
def crear_tabla():
    return render_template('crear_tabla.html')
"""
@app.route("/eliminar/<tabla>/<id>")
@login_required
def eliminar(tabla,id):
	print("========TABLA==========",tabla)
	conn=conexion()
	where="id= "+id
	conn=conn.delete(tabla,where)
	if conn:
		flash('Se ha eliminado correctamente', 'success')
	else:
		flash('No se elimino ningún registro', 'danger')
	return redirect(url_for('opciones'))

@app.route('/editar_reg/<id>/<tabla>',methods=['GET','POST'])
@login_required
def editar_reg(id,tabla):

	form = editar_vehiculo_form()
	conn=conexion()
	where="id= "+id
	conn=conn.select("*",tabla,where,"2")
	print("EDITAR============", conn)

	if form.validate_on_submit():

		modelo=form.modelo.data
		marca=form.marca.data
		año=str(form.año.data)
		precio=str(form.precio.data)
		where="id ="+id
		conn=conexion()
		conn = conn.update(tabla,where,modelo, marca, precio,año)
		flash('Se ha editado correctamente', 'success')
		return redirect(url_for('ver',opcion=tabla))
		#Alert diciendo que el usuario se creo correctamente
	return render_template('editar_vehiculos.html', form=form, info=conn,title="Editar")