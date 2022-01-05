class Persona:
    #variables > atributos 
    def saludar(self):
        #funciones son metodos
        print("hola", self.nombre )

    #constructor
    def __init__(self, nombre, edad, estatura, sexo = "gi") :
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.sexo = sexo


# cuando una variable  le asignamos una clase pasa a llamar una instancia de la clase (copia de la clase con todos sus atributos y metodos)
eduardo  = Persona(nombre = "Julio", edad = 12,  estatura = 1.65)

print(eduardo.nombre)
print(eduardo.sexo)
eduardo.sexo= "machazo"
print(eduardo.sexo)
eduardo.saludar()





