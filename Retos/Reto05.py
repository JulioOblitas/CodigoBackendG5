from flask import  Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

listadatos = []

@app.route('/registrodatos', methods = ['POST'])

def registrar():
    if request.method =='POST':
            data = request.get_json()
            listadatos.append(data)
            return{
                'data' : listadatos,
                'message' : 'Datos Agregados',
                'ok' : True
            },201   

@app.route('/listadodatos', methods = ['GET'])
def listado():
    if request.method =='GET':            
            
            return{
                'data' : listadatos,
                'message' : 'Listado de Datos',
                'ok' : True
            },201   


if __name__ == "__main__":
    app.run(debug=True, port = 3000)