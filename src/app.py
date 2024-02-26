from flask import Flask, render_template #Es para importar flask

app = Flask(__name__) #creamos una instancia de flask en una variable llamada app(se puede llamar como sea)

@app.route('/')#usamos un decorador(@) para crear una respuesta a la ruta / que es el index o página principal
def Hola(): #creamos la función que va a responder al llamado a  la ruta /
    return '<h1>Hola mundo</h1>' #es lo que devuelve la función es este caso solo un texto (hola mundo)
@app.route('/plantilla')
def plantilla():
    data={
        'titulo':'Practica #2 con Bootstrap',
        'mensaje':'Bienvenido al sitio Web ',
        'nombre':'Dorian Fernando Galindo Salinas'
    } #Declaración de diccionario
    return render_template('layout.html',data=data) #render_template es para renderizar la plantilla

@app.route('/datos/<nombre>')
def datos(nombre):
    data={
        'titulo':'Datos del Estudiante',
        'matricula':'04220026',
        'nombre':nombre,
        'correo':'l0400220026@progreso.tecnm.mx'
    }
    return render_template('datos.html',data=data)

@app.route('/index')
def index():
    data={
        'titulo':'Página Principal',
        'mensaje':'Bienvenido, esta es la página principal.'
    }
    return render_template('index.html',data=data)

def error404(error):
    return render_template('404.html'), 404
app.register_error_handler(404, error404)
app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual

    
    
    #recuerda que para verlo solo debemos entrar a la dirección 127.0.0.1:5000 en cualquier navegador
    #es importante crear la carpeta templates porque ahi va flask a intentar buscar el archivo de la plantilla.