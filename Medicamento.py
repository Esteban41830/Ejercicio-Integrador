class Medicamento:
    __idCama = 0
    __idMedicamento = 0
    __NombreComercial = ''
    __Monodroga = ''
    __Presentacion = ''
    __CantidadAplicada = 0
    __Precio = 0.0
    
    def __init__(self,idCama,idComercial,NombreComercial,Monodroga,Presentacion,
                 CantidadAplicada,Precio):
        
        self.__idCama = idCama
        self.__idMedicamento = idComercial
        self.__NombreComercial = NombreComercial
        self.__Monodroga = Monodroga
        self.__Presentacion = Presentacion
        self.__CantidadAplicada = CantidadAplicada
        self.__Precio = Precio
    
    def getID(self):
        return self.__idCama
    
    def getPrecio(self):
        return self.__Precio

    
    def __str__(self):
        return '{}{:20}{:20}{:20}'.format(self.__Monodroga,self.__Presentacion,self.__CantidadAplicada,self.__Precio)
        
        