# Aplicación Flask

from flask import Flask, request, render_template
import mysql.connector
from mysql.connector.errors import IntegrityError

app = Flask(__name__)

@app.route('/',methods=["GET"])
def inicio():
    return render_template("form.html",errormesaje=" ")

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

  try:
    # Crear consulta de inserción
    query = "INSERT INTO registro (servidor, plugin, version, fecha, obsoleto, premium, db) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (servidor, plugin, version, fecha, obsoleto, premium, db)

    # Conectarse a la base de datos y ejecutar consulta
    conn = mysql.connector.connect(host='192.168.50.29', user='taskuploguser', password='taskuplogpass', database='taskuplogdb')
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
  except IntegrityError:
    return render_template("form.html",errormesaje="Error: Registro Duplicado")

  # Cerrar cursor y conexión
  cursor.close()
  conn.close()
  
  return render_template("form.html",errormesaje=" ")

# Ruta que realiza la consulta a la db
@app.route('/query', methods=['GET','POST'])
def query():
  # Crear consulta de inserción
  query = "select servidor,plugin,version,fecha,obsoleto,premium,db from registro"

  # Conectarse a la base de datos y ejecutar consulta
  conn = mysql.connector.connect(host='192.168.50.29', user='taskuploguser', password='taskuplogpass', database='taskuplogdb')
  cursor = conn.cursor()
  cursor.execute(query)
  row=cursor.fetchall()
  listadatos = []
  for rows in row:
    listadatos.append(rows)
  # Cerrar cursor y conexión
  cursor.close()
  conn.close()
  
  return render_template("query.html",datos=listadatos,errormesaje=" ")

if __name__ == '__main__':
  app.run("0.0.0.0",5000,debug=True)
