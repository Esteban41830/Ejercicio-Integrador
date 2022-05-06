import Cama
import ManejadorMedicamento
import csv

class ManjadorCama:
    def __init__(self):
        self.__ListaCama = []
        
    def AgregarCama(self,unaCama):
        self.__ListaCama.append(unaCama)
        
    def CargaCama(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            idcama = fila[0]
            Habitacion = fila[1] 
            Estado = fila[2]
            Apellido = fila[3]
            Nombre = fila[4]
            Diagnostico = fila[5]
            FI = fila[6]
            FA = fila[7]
            unaCama = Cama.Cama(idcama,Habitacion,Estado,Apellido,Nombre,Diagnostico,FI,FA)
            self.agregar(unaCama)
         
        archivo.close()
    
    def BuscarPaciente(self,Nombre,Apellido):
        V = False
        i = 0
        while (V == False) and (i in range(len(self.__ListaCama))):
            if (self.__ListaCama[i].getNombre == Nombre) and (self.__ListaCama[i].getApellido == Apellido):
                V = True
            else:
                i+=1
        
        if i > len(self.__ListaCama):
            print('El paciente no se encuentra')
        else:
            self.__ListaCama[i].DatosPaciente()
            print('{}{:20}{:20}{:20}'.format('Medicamento/Monodroga','Presentacion','Cantidad','Precio'))
            total = ManejadorMedicamento.BucaMedicamento(self.__idCama)
            print('Total Adeudado......................................{}'.format(total))
            
    
    def ListadoPaciente(self,diagnostico):
        for i in range(len(self.__ListaCama)):
            if self.__ListaCama[i].getDiagnostico == diagnostico:
                self.__ListaCama[i].DatosPaciente()     