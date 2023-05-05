import Materia as MM 
import csv
import ManejadorAlumnos as MA

class ManejaMaTeria:
    def __init__(self):
        self.__Materias = []
        
    def agregaMateria(self,unaMateria):
        self.__Materias.append(unaMateria)
        
    
    def testMaterias(self):
        
        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        
        for fila in reader:
            unaMateria = MM.Materia(fila[0], fila[1], fila[2],fila[3], fila[4])
            self.agregaMateria(unaMateria)
        
        archivo.close()
    
    
    def promedio(self,documento):
        notaA = 0
        notaB = 0
        cant = 0
        for i in range(len(self.__Materias)):
            if documento == self.__Materias[i].getDNI():
                notaA = notaA +self.__Materias[i].getNota()
                if self.__Materias[i].getNota() < 4:
                    notaB = notaB+self.__Materias[i].getNota()
            
                cant = cant+1
        print('Sin aplazo: {}'.format((notaA-notaB)/cant))
        print('Con aplazo: {}'.format(notaA/cant))
    
    def informe(self,nom):
        
        print('\n{:10}{:20}{:10}{:10}{:10}'.format('DNI','Apeliido y Nombre','Fecha','Nota','Año que cursa'))
        for i in range(len(self.__Materias)):
            print('{}'.format(self.__Materias[i].getNombre))
            print('{}'.format(self.__Materias[i].getNota))
            if self.__Materias[i].getNombre == nom and self.__Materias[i].getNota >= 7:
                print('entro en el if')
                nota = self.__Materias[i].getNota 
                fecha = self.__Materias[i].getFecha()
                dni = self.__Materias[i].getDNI()
                MA.mostarInforme(nota,fecha,dni)