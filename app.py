# Aplicación Flask

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Ruta que maneja el envío del formulario
@app.route('/insertar', methods=['POST'])
def insertar():
  # Recoger datos del formulario
  servidor = request.form['server']
  plugin = request.form['plugin']
  version = request.form['version']
  fecha = request.form['date']
  obsoleto = 1 if 'obsolete' in request.form else 0
  premium = 1 if 'premium' in request.form else 0
  db = 1 if 'db' in request.form else 0

  # Crear consulta de inserción
  query = "INSERT INTO tabla (servidor, plugin, version, fecha, obsoleto, premium, db) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  values = (servidor, plugin, version, fecha, obsoleto, premium, db)

  # Conectarse a la base de datos y ejecutar consulta
  conn = mysql.connector.connect(host='localhost', user='usuario', password='contraseña', database='nombre_de_la_bd')
  cursor = conn.cursor()
  cursor.execute(query, values)
  conn.commit()

  # Cerrar cursor y conexión
  cursor.close()
  conn.close()
  
  return 'Información insertada correctamente'

if __name__ == '__main__':
  app.run()
