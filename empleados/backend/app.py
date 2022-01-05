
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

app =  Flask (__name__)
CORS(app=app)

usuarios = []

@app.route('/listausuarios', methods = ['GET','POST']) 
def getusuarios():
    if request.method =="GET":
        response = usuarios
        return jsonify(response)
    elif request.method == 'POST':
        data = request.get_json()

        print(data)
        usuarios.append(data) # insertando un registro en una bd (INSERT INTO ...)
        
        return {
            'data': usuarios,
            'message': 'Usuario Agregado exitosamente',
            'ok': True
        }, 201


@app.route('/eliminaruser/<string:dni>', methods = ['DELETE']) 
def geteliminar(dni):
    
    z = 0
    pos = 0
    for x in usuarios:
         #print(x["dni"])
        z = z + 1  
        if x["dni"] == dni:     
        # print(data[z-1])  
            pos = z-1 
        break
        #print(pos)
    nuevalista = usuarios.pop(pos)
        #print(data)
    
    if request.method =="DELETE":        
        return {
            'data': nuevalista,
            'message': 'Usuario Eliminado exitosamente',
            'ok': True
        }
    




if __name__ == '__main__':
    app.run (debug=True)