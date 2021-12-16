from datetime import datetime

nombre = input("Ingrese Nombre: ")
edad = input("Ingrese Edad : ")


# se obtiene la hora en formato de 24 horas 
valor = datetime.now().strftime('%H')


if  int(edad) <18 and int(valor) < 19 :

    print( nombre.upper() , " Vete a dormir ... Cachorro")
else:
     print( nombre.upper(), "Eres Adulto haz de tu vida lo que quieras")