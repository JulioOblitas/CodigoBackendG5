from datetime import  datetime

anoactual = datetime.now()
ano = int(anoactual.strftime(" %Y"))

cant =  input ("Ingrese Cantidad para Lista : ")
personas= []
for  i in range(0,int(cant)):
    
    nombre =  input ("Nombre : ")
    dni =     input ("Dni  : ")
    fecha =   input ("Fecha de Nacimiento : ")

    fechanac = int(fecha[6:10])
    edad = ano - fechanac

    personas.append({
        'nombre': nombre,
        'dni': dni,
        'fecha': fecha,
        'edad' : edad
    })




# 
def get_edad(personas):
    return personas.get('edad')

personas.sort(key=get_edad)
#print(personas, end='\n\n') 

listado=[]
for persona in personas:
        
        listado.append({    
        'nombre': persona['nombre'],        
        'edad' : persona['edad']
    })


print(listado)
