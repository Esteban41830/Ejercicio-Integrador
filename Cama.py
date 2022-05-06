class Cama:
    __idCama = 0
    __Habitacion = 0 
    __Estado = False
    __Apellido = ''
    __Nombre = ''
    __Diagnostico = ''
    __FechaInternacion = ''
    __FechaAlta = ''
    
    def __init__(self,idCama,Habitacion,Estado,Apellido,Nombre,Diagnostico,FechaInternacion,
                 FechaAlta):
        
        self.__idCama = idCama
        self.__Habitacion = Habitacion
        self.__Apellido = Apellido
        self.__Nombre = Nombre
        self.__Diagnostico = Diagnostico
        self.__FechaInternacion = FechaInternacion
        self.__FechaAlta = FechaAlta
    
    
    def getNombre(self):
        return self.__Nombre


    def getApellido(self):
        return self.__Apellido
    
    
    def getDiagnostico(self):
        return self.__Diagnostico
    
    def DatosPaciente(self):
        print('Paciente:{},{}       Cama: {}            Habitacion:{}'.format(self.__Apellido,self.__Nombre,
                                                                       self.__idCama,self.__Habitacion))
        print('Diagnostico: {}      Fecha de Internacion: {}'.format(self.__Diagnostico,self.__FechaInternacion))
        print('Fecha de Alta: {}\n'.format(self.__FechaAlta))

    
    

    
