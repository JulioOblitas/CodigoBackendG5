from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app=app)  

listaproductos =[{
    "id" : 1,
    "nombre":"Paneton Donofrio",
    "precio": 17,
    "disponible" : True,
    "fecven": "2022-01-14"
},
{    
    "id" : 2,
    "nombre":"Paneton Motta",
    "precio": 20.50,
    "disponible" : True,
    "fecven": "2022-01-14"
},
]

@app.route('/productos', methods = ['POST', 'GET'])

def inicio():

    if request.method =='POST':
            data = request.get_json()
            listaproductos.append(data)
            return{
                'data' : listaproductos,
                'message' : 'Producto Agregado',
                'ok' : True
            },201            
    elif request.method == 'GET':
            return{
                'data' : listaproductos,
                'message' : 'Los productos son',
                'ok' : True
            }
    
                
@app.route('/producto/<int:id>',methods = ['GET', 'PUT' ,'DELETE']) 
def producto(id):
    none = ""
    if request.method =='GET':
        #    return {'id' : id}

        if (id < len(listaproductos)):
            return{
            'ok' : True,
            'data' : listaproductos[id],
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
        if (id<len(listaproductos)):
            listaproductos[id] = data #sobreescribir datos
            return {
                'ok' : True,
                'Data' :    listaproductos[id],
                'message' : 'Producto Actualizado'
            },201
        else:
             return {
                'ok' : False,
                'Data' :    None,
                'message' : 'Producto con el id {}  no existe ' .format(id)
                }
    elif request.method == 'DELETE':
            if (id<len(listaproductos)):
                listaproductos.pop(id)
                return {
                'ok' : True,
                'Data' :   listaproductos,
                'message' : 'Producto Eliminado'
                },200
            else:
                return {
                'ok' : False,
                'Data' :    None,
                'message' : 'Producto con el id {}  no existe ' .format(id)
                },200

if __name__ == "__main__":
    app.run(debug=True, port = 3000)

