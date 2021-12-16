numero1= 80
numero2 =35
resultado = numero1+ numero2

#impresion claisco
print(resultado)
print('El resultado es', resultado) 

#impresion format usando llaves  se usa mas 
print ('El resultado es {} y nada mas {}'.format(resultado,numero1))

#impresion format en abreviado  usando llaves se usa mas
print(f'el resultado es {resultado}')

#impresion en el orden de los elementos de la lista
print ('El resultado es {1} y nada mas {0}'.format(numero1,resultado))

resultado = numero1 - numero2
resultado = numero1 * numero2
resultado = numero1 / numero2

#el modulo
resultado = numero1 % numero2

#el cociente
resultado = numero1 // numero2
print('El cocients es ', resultado  )

#mostrar resultados 
print('{:.3f}'.format(resultado))
print(f'{resultado:.4f}')

texto = "Hola mi nombre es eduardo "

print(texto[:5])
print(texto[0:5])

