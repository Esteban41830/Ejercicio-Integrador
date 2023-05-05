class Alumno:
    __dni = 0
    __Apellido = ''
    __Nombre = ''
    __Carrera = ''
    __Año = ''
    
    def __init__(self,dni,apell,nom,carr,año):
        self.__dni = int(dni)
        self.__Apellido = apell
        self.__Nombre = nom
        self.__Carrera = carr
        self.__Año = int(año)
    
    
    def getDNI(self):
        return self.__dni
    
    def getApellido(self):
        return self.__Apellido
    
    def getNombre(self):
        return self.__Nombre
    
    def getAño(self):
        return self.__Año
    
    def __gt__(self,otro):
        return self.__Apellido < otro.__Apellido
    
    def __str__(self):
        return '{},{}  {}, {} {}\n'.format(self.__Apellido,self.__Nombre,self.__dni,self.__Carrera,self.__Año)
    
    