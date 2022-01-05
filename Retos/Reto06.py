from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)

listatareas = []
@app.route('/registrotarea', methods = ['POST'])
def registrartarea():
    if request.method =='POST':
            data = request.get_json()
            listatareas.append(data)
            return{
                'data' : listatareas,
                'message' : 'Tarea Agregada',
                'ok' : True
            },201   

@app.route('/listartarea', methods = ['GET'])
def listartarea():
    if request.method =='GET':                 
            return{
                'data' : listatareas,
                'message' : 'Lista de Tareas',
                'ok' : True
            },201   

@app.route('/tareas/<int:id>',methods = ['GET', 'PUT' ,'DELETE']) 
def tareas(id):
    none = ""
    if request.method =='GET':
        
        if (id < len(listatareas)):
            
            return{
            'ok' : True,
            'data' : listatareas[id],
            'message' : 'Listado de Tareas'
        }
        else:
            return{
            'ok' : False,
            'data' : none,
            'message' : 'Tarea no existe'

        }
    elif request.method == 'PUT':
        data = request.get_json()
        if (id<len(listatareas)):
            listatareas[id] = data #sobreescribir datos
            return {
                'ok' : True,
                'Data' :    listatareas[id],
                'message' : 'Tarea Actualizada'
            },201
        else:
             return {
                'ok' : False,
                'Data' :    None,
                'message' : 'Tarea con el id {}  no existe ' .format(id)
                }
    elif request.method == 'DELETE':
            if (id<len(listatareas)):
                listatareas.pop(id)
                return {
                'ok' : True,
                'Data' :   listatareas,
                'message' : 'Tarea Eliminada'
                },200
            else:
                return {
                'ok' : False,
                'Data' :    None,
                'message' : 'Tarea con el id {}  no existe ' .format(id)
                },200


if __name__ == "__main__":
    app.run(debug=True, port = 3000)