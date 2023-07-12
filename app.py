from flask import Flask, render_template
import pyodbc
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Inicializar la aplicación de Firebase
cred = credentials.Certificate('nicadrinks-a6375-firebase-adminsdk-azgt0-0ceff29b66.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'nicadrinks-a6375.appspot.com'})

# Establecer la configuración de la conexión a SQL Server
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-TMBOKVK\\SQLEXPRESS;'
    'Database=DBNICADRINKS;'
    'UID=;'
    'PWD=;'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienessomos')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/ronflor')
def ronflor():
    # Consultar los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, precio, descripcion, imagen_url FROM productos')
    productos = cursor.fetchall()
    cursor.close()

    # Generar las URLs de las imágenes desde Firebase Storage
    bucket = storage.bucket()
    
    for producto in productos:
        imagen_url = producto.imagen_url
      
    # Renderizar la plantilla con los productos y sus imágenes
    return render_template('ronflor.html', productos=productos)

@app.route('/ronplata')
def ronplata():
    # Consultar los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, precio, descripcion, imagen_url FROM productos')
    productos = cursor.fetchall()
    cursor.close()

    # Generar las URLs de las imágenes desde Firebase Storage
    bucket = storage.bucket()
    
    for producto in productos:
        imagen_url = producto.imagen_url
      
    # Renderizar la plantilla con los productos y sus imágenes
    return render_template('ronplata.html', productos=productos)

@app.route('/aguaardiente')
def aguaardiente():
    # Consultar los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, precio, descripcion, imagen_url FROM productos')
    productos = cursor.fetchall()
    cursor.close()

    # Generar las URLs de las imágenes desde Firebase Storage
    bucket = storage.bucket()
    
    for producto in productos:
        imagen_url = producto.imagen_url
      
    # Renderizar la plantilla con los productos y sus imágenes
    return render_template('aguaardiente.html', productos=productos)

@app.route('/cervezas')
def cervezas():
    # Consultar los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, precio, descripcion, imagen_url FROM productos')
    productos = cursor.fetchall()
    cursor.close()

    # Generar las URLs de las imágenes desde Firebase Storage
    bucket = storage.bucket()
    
    for producto in productos:
        imagen_url = producto.imagen_url
      
    # Renderizar la plantilla con los productos y sus imágenes
    return render_template('cervezas.html', productos=productos)

@app.route('/productos')
def productos():
    # Consultar los productos desde la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, precio, descripcion, imagen_url FROM productos')
    productos = cursor.fetchall()
    cursor.close()

    # Generar las URLs de las imágenes desde Firebase Storage
    bucket = storage.bucket()
    
    for producto in productos:
        imagen_url = producto.imagen_url
      
    # Renderizar la plantilla con los productos y sus imágenes
    return render_template('productos.html', productos=productos)