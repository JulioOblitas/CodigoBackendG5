#comentario
numero = 10;
numero2 = 10.5;


valor = True
nombre = """ jose 
martin oblitas """

print("hola")
print(numero)
print(nombre)
print(type(nombre))
print(type(valor))
print(type(numero))
print(type(numero2))

#declarando arreglos o LIST 
edades = [10,12,13,14, 'Eduardo', 14.50, False, [1,2] ]


#Json  (JavaScript Object Notation  ) | Diccionario
curso = {
    'nombre' : 'Backend',
    'dificultad' : 'Dificil',
    'skills'  : [
        {
            'nombre' :'Base de Datos',
            'nivel' : 'Intermedio'
        },
        {
            'nombre' :'ORM',
            'nivel' : 'Avanzado'
        }
    ]
}
print(curso)

print(curso['nombre']);

print(edades[1:-1])

valor = curso['skills'][1]['nivel'];

print(valor)



personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]



nacion = personas[1]['hobbies'];

print(nacion)

