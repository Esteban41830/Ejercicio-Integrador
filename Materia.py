class Materia:
    __dni = 0
    __nombre = ''
    __fecha = ''
    __nota = 0.0
    __aprobacion = ''
    
    def __init__(self,dni,nom,fecha,nota,apro):
        self.__dni = int(dni) 
        self.__nombre = nom
        self.__fecha = fecha 
        self.__nota = int(nota)
        self.__aprobacion = apro
    
    
    def getDNI(self):
        return self.__dni
    
    
    def getNota(self):
        return self.__nota
    
    def getNombre(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fecha
    
    
    