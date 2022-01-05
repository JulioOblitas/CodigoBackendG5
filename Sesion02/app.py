from flask import Flask, render_template,request,redirect,url_for

from productos import Productos
app = Flask(__name__)

lista_productos = [

    Productos('COMPUTADOR', 'COMPUTADOR 5TA GENERACION ' , 2700),
    Productos('IMPRESORA', 'EPSON STYLLUS  ' , 700),
    Productos('USB', 'USB SAMSUNG ' , 80),
]

@app.route("/")
def index():
    return render_template('lista_productos.html', productos = lista_productos)

app.run(debug=True)