import mysql.connector 
from proyecto.users import user

from proyecto import login_manager
@login_manager.user_loader
def load_user(user_id):
  conn=conexion()
  where="id="+user_id
  #Se crea el objeto usuario y se almacena en la variable usuario
  usuario=conn.select("*","usuarios",where,"1")
  print()
  return usuario



class conexion:

    def __init__(self):
      self.ht="localhost"
      self.db="proyectotopico"
      self.usuario="root"
      self.password=""

      self.conexion = mysql.connector.connect(host=self.ht,
                                             database=self.db,
                                             user=self.usuario,
                                             password=self.password)

#BANDERA: 1.- PARA SELECT, 2.-PARA INSERT o Hacer Commit

    def ejecutar_query(self, query,bandera):
      cursor=self.conexion.cursor()
      try:
        cursor.execute(query)
        if bandera is "2":
          #print("QUERY INSERT")
          self.conexion.commit()
          return True
        else:
          #print("QUERY SELECT")
          return cursor
      except self.conexion.Error as err:
        print("Something went wrong: {}".format(err))

# METODO SELECT
#  columna: atributo usado de referencia
#  where: condicion 2 posibles casos("contraseña = 123 and email =uaq@gmail.com" ó "1")
#  tabla: tabla a la que se hara la consulta
#  bandera: 1.- retorna toda la fila de la bd (usado para instanciar el objeto User)
#                                             "columna = *" obligatoriamente
#           2.- retorna todos los registros
#           3.- retorna un unico registro si existe (usado para obtener contraseña hasheada)
        

    def select(self, columna,tabla, where,bandera):

      query=("SELECT "+columna+" from "+tabla+" WHERE "+where)
      #print("QUERY==",query)
      if bandera is "1":
        #print(query)
        cursor= self.ejecutar_query(query,"1")
        data = cursor.fetchone()
        cursor.close()
        usuario=user(data[0],data[1],data[2],data[3],data[4],data[5])
        return usuario
      elif bandera is "2":
        cursor= self.ejecutar_query(query,"1")
        data = cursor.fetchall()
        cursor.close()
        return data
      elif bandera is "3":
        cursor= self.ejecutar_query(query,"1")
        resultado = cursor.fetchone()
        data= str(resultado[0])
        return data

    def insert_vehiculos(self,tabla, modelo, marca, precio, year):
 
      query=("INSERT INTO "+tabla+" VALUES (NULL,'"+modelo+"', '"+marca+"', "+year+", "+precio+")")
      
      result=self.ejecutar_query(query,"2")

    def insert_usuarios(self, nombre, apellidos, password, email, privilegios):

      query=("INSERT INTO usuarios (nombre, apellidos, contraseña, email,privilegios) "
            "VALUES ('"+nombre+"','"+apellidos+"', '"+password+"', '"+email+"', "+privilegios+")")
      
      result=self.ejecutar_query(query,"2")

    def delete(self,tabla,where):

      query=("DELETE FROM " +tabla +" WHERE "+where)
      print("QUERY=== DELETE",query)
      result= self.ejecutar_query(query,"2")
      return result

    def update(self,tabla,where,modelo,marca,precio,año):

      query=("UPDATE "+tabla+" SET Modelo ='" +modelo +"', Marca='"+marca+"',año='"+año+
        "', precio='"+ precio +"' WHERE "+where)

      print("QUERY=== UPDATE",query)
      result= self.ejecutar_query(query,"2")
      return result