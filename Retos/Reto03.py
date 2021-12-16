cant = int(input("Cantidad de Prod a Ingresar : "))
i=1

#Creando objeto
class  productos:
    def __init__(self, descripcion):
        self.descripcion=descripcion

    def imprimirdescripcion (self):
        
        print(self.descripcion , " producto de alta calidad")



while  i <= cant:
        producto = input(" Producto : " )

        prod = productos(producto)

        prod.imprimirdescripcion()

        rpta = input(" Desea Salir S/N : " )

        if rpta.upper() == "S":
            break

        i =i +1

