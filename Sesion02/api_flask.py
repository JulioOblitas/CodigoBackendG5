from flask import Flask , request
from flask_cors import CORS
#NOS DA TODA LA INFORMACION DEL CLIENTE 
app = Flask(__name__)

CORS(app=app)  

#url es el dominio + el endpoit
usuarioslista = []
mis_productos = [{
    "id" : 1,
    "nombre":"Paneton con arto bromato",
    "precio": 17.50,
    "disponible": True,
    "fecha_vencimiento": "2022-01-14"
}, {
        "id" : 2,
    "nombre":"Chocolate con arta azucar",
    "precio": 6.90,
    "disponible": False,
    "fecha_vencimiento": "2021-12-30"
}]


@app.route('/', methods = ['POST', 'GET'])
def inicio():
    
    print(request.method)
    if request.method == 'POST':

        print(request.get_json())

        data = request.get_json()

        # get()> sirve para extraer la informacion de un diccionario segun su llave  y sino existe su  lllave
        #retona vacio o null , ADCIONAL COMO SEGUNDO PARAMETRO SE PUEDE INDICAR EL VALOR SI ES QUE NO EXISTE 

        if (data.get('nombre')):
            nombre  = data['nombre']
            return 'Hola, {}!' .format(nombre)

        else:
         
            return 'NECESITO INFORMACION'
    elif request.method == 'GET':

    #cuando retornamos una rpta  puede contener hasta 2 parametro
    # uno es la data y el otro codigo htpp
        return 'Bienvenido al API DE PRODUCTOS' , 404

@app.route('/listausuarios', methods = ['GET','POST'])
def usuariosregistrar():
        if request.method == 'GET':

            return{
                'data' : mis_productos,
                'message' : 'Los productos son',
                'ok' : True
            }
        elif  request.method == 'POST':
            data  = request.get_json()
            usuarioslista.append(data)
            return{
                'data' : usuarioslista,
                'message' : 'Producto Agregado',
                'ok' : True
            },201        

@app.route('/productos', methods = ['GET','POST'])
def productos():
        if request.method == 'GET':
            return{
                'data' : mis_productos,
                'message' : 'Los productos son',
                'ok' : True
            }
        elif  request.method == 'POST':
            data  = request.get_json()
            mis_productos.append(data)
            return{
                'data' : mis_productos,
                'message' : 'Producto Agregado',
                'ok' : True
            },201

@app.route('/producto/<int:id>',methods = ['GET', 'PUT' ,'DELETE']) 
def producto(id):
    none = ""
    if request.method =='GET':
        #    return {'id' : id}

        if (id < len(mis_productos)):
            return{
            'ok' : True,
            'data' : mis_productos[id],
            'message' : 'el producto es XX'
        }
        else:
            return{
            'ok' : False,
            'data' : none,
            'message' : 'el producto no existe'

        }
    elif request.method == 'PUT':
        data = request.get_json()
        if (id<len(mis_productos)):
            mis_productos[id] = data #sobreescribir datos
            return {
                'ok' : True,
                'Data' :    mis_productos[id],
                'message' : 'Producto Actualizado'
            },201
        else:
             return {
                'ok' : False,
                'Data' :    None,
                'message' : 'Producto con el id {}  no existe ' .format(id)
                }

            




#validar el contenido de la variable main se main
if __name__ == "__main__":
    app.run(debug=True)


