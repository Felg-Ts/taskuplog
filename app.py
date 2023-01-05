#connection

import mysql.connector
from mysql.connector import errorcode

def connect():
    try:
        cnx = mysql.connector.connect(user='your-username',
                                      password='your-password',
                                      host='your-host',
                                      database='your-database')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def execute_query(query, params):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(query, params)
    cnx.commit()
    cursor.close()
    cnx.close()

#Ruta De Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Comprobar si el nombre de usuario y la contraseña son válidos
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        params = (username, password)
        result = execute_query(query, params)

        # Si se obtiene un resultado, iniciar sesión
        if result:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))

        # Si no se obtiene un resultado, mostrar mensaje de error
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    # Si el método es GET, mostrar formulario de inicio de sesión
    return render_template('login.html')
