import Medicamento
import csv

class ManejadorMedicamento:
    def __init__(self):
        self.__ListaMedicamento = []

    def AgregarMedicamento(self,unMedicamento):
        self.__ListaMedicamento.append(unMedicamento)
        
    def CargaMedicamento(self):
        archivo = open('medicamento.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            idCama = fila[0]
            idMedicamento = fila[1]
            NombreComercial = fila[2]
            Monodroga = fila[3]
            Presentacion = fila[4]
            CantidadAplicada = fila[5]
            PrecioTotal = fila[6]
            unMedicamento = Medicamento.Medicamento(idCama,idMedicamento,NombreComercial,Monodroga,
                                             Presentacion,CantidadAplicada,PrecioTotal)
            self.Agregar(unMedicamento)
        
        archivo.close()
    
    
    def BucaMedicamento(self,ID):
        total = 0.0
        for j in range(len(self.__ListaMedicamento)):
            if self.__ListaCama[j].getID == ID:
                print(self.__ListaMedicamento[j])
                total += self.__ListaMedicamento[j].getPrecio
        
        return total