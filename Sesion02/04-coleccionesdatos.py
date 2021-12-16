dias = ['Lunes', 'martes', 'miercoles']

#agregar valores
dias.append('Jueves')
print(dias)
#eliminar valores
dias.remove('martes')
print(dias)


otros_dias = ['Sabado', 'Domingo']
# para combinar dos listas  usar mas 
dias_semana = dias  + otros_dias

dias.clear()
print(dias)
print(dias_semana)

#tuplas
#coleccion igual que la lista PERO LA TUPLA NO SE PUEDE MODIFICAR
alumnos  = ('Eduardo', 'Pedro', 'Ana', 'Roberta')

CONFIGURACION = (
    {
        'NOMBRE':'APIKEY',
        'VALOR' :'XXXXXXXXX'
    },
    {
        'NOMBRE':'APIKEY',
        'VALOR' :'ZZZZZZZZZZZ'
    }

)


CONFIGURACION = ('aaaaa','fgfgfgf','dfgfgfgfgfg')
#alumnos[0] = 'JULIO'
#CONFIGURACION [0]['NOMBRE'] = 'XD'



print(alumnos)
print(CONFIGURACION[0])
print(CONFIGURACION)



#variasbles mutables / inmutables
lista1  = [1,2,3,4,5]
lista2  = lista1
lista3  = lista1[:]
print(lista1)
print(lista2)
print(lista3)

lista1[0] = 50

#para ver el area de  memoria
print(id(lista1))
print(id(lista2))
print(id(lista3))

print('la lista 1 es ' , lista1)
print('la lista 2 es',lista2)
print('la lista 3 es',lista3)

# Variables inmutables son las variables de tipo primitivo como los INT, STR, FLOAT, BOOLEAN, DATE..
nombre1= 'Eduardo'
nombre2 = nombre1
nombre1 = 'Ruben'

print(nombre1)
print(nombre2)
print(id(nombre1))
print(id(nombre2))

# DICCIONARIOS
# coleccion de elementos que estan INDEXADOS cuentan con una LLAVE (o clave) y su valor o contenido, se pueden modificar el contenido y ademas se puede crear nuevas llaves
persona= {
    'nombre': 'Eduardo',
    'correo': 'ederiveroman@gmail.com',
    'direcciones': [
        {
            'calle': 'xxxx 1234',
            'dpto': 'arequipa'
        },
        {
            'calle': 'yyyyy 4567',
            'dpto': 'lima'
        }
    ],
    'est_civil': 'soltero'
}
persona['estatura']= '1.95'

print('Para saber las llaves del diccionario:',persona.keys())
print('Para saber el contenido de todo el diccionario:', persona.values())

#conjuntos 
colores  = {'rojo', 'verde', 'amarillos'}
colores.remove('verde')
colores.add('mostaza')
print(colores)