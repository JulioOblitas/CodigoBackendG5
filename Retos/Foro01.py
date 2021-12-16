class  persona:
    def __init__(self, nombre, sexo, fechanac, tipo):
        self.nombre =nombre
        self.sexo  = sexo
        self.fechanac = fechanac
        self.tipo = tipo

    def saludo(self):
            if self.tipo == "PROFESOR":
                print("Hola soy el profesor", self.nombre )
            else:
                print("Hola soy el alumno", self.nombre )




class profesor(persona):
     def  __init__(self, especialidad):         
        self.especialidad = especialidad
        
     def especialista(self):            
        print("Especialista", self.especialidad)
            
    
class alumno(persona):
     def  __init__(self, curso):         
        self.curso = curso

     def cursos(self):            
        print("Curso", self.curso)


objetoprofesor =  profesor("BACKEND")
objetoprofesor.nombre = "EDUARDO RIVERO"
objetoprofesor.fechanac= "23/05/1985"
objetoprofesor.tipo = "PROFESOR"
objetoprofesor.sexo = "M"
objetoprofesor.saludo() 
objetoprofesor.especialista()

#objeto alumno

objetoalumno =  alumno("NODE JS")
objetoalumno.nombre = "JULIO OBLITAS"
objetoalumno.fechanac= "23/05/1978"
objetoalumno.tipo = "ALUMNO"
objetoalumno.sexo = "M"
objetoalumno.saludo() 
objetoalumno.cursos()


    

