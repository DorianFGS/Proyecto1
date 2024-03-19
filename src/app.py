from flask import Flask, render_template, request, redirect, url_for, session, flash
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_USER"]= config.MYSQL_USER
app.config["MYSQL_DB"]= config.MYSQL_DB
app.config["MYSQL_PASSWORD"]= config.MYSQL_PASSWORD
app.config['SECRET_KEY'] = config.HEX_SEC_KEY

mysql = MySQL(app)

@app.route('/') 
def index(): 
    data={
        'titulo':'Página Principal',
        'mensaje':'Bienvenido, esta es la página principal.'
    }
    return render_template('index.html', data=data)

@app.route('/login', methods=['POST','GET'])
def login():
    email=request.form.get("email")
    password= request.form.get("password")
    cur=mysql.connection.cursor()
    cur.execute("select * from users where email= %s and password=%s", (email,password))
    user=cur.fetchone()
    cur.close()
    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]

        return redirect(url_for('home'))
    else:
        flash("Error de Contraseña")
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

def error404(error):
    return render_template('404.html'), 404
app.register_error_handler(404, error404)
app.run(debug=True) 

if __name__ =='__main__':
    app.run(debug=True)