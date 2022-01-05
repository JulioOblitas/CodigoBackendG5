from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)
listadptos = ['Amazonas','Ancash','Apurimac','Arequipa','Ayacucho','Cajamarca','Callao','Cusco','Huancavelica', 'Huanuco', 'Ica', 'Junin','La Libertad',
'Lambayeque','Lima','Loreto','Madre de Dios','Moquegua','Pasco', 'Piura','Puno','San Martin','Tacna','Tumbes','Ucayali']


@app.route('/departamentos',methods = ['GET'])
def inicio():

    if request.method == 'GET':
            return{
                'content' : listadptos,
                'message' : 'Los departamentos son',
                'ok' : True
            }
    
if __name__ == "__main__":
    app.run(debug=True, port = 3000)

