import Alumno
import csv
import numpy as np

class ManejaAlum:  
    __cantidad = 0
    __dimension = 0
    __incremento = 0
    
    def __init__(self,dimension = 10,incremento = 5):
        self.__Alumnos = np.empty(dimension, dtype = Alumno.Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        
    def agregaAlumno(self,unAlumno):
        if self.__cantidad == self.__dimension:
            self.__dimension +=self.__incremento
            self.__Alumnos.resize(self.__dimension)
            
        self.__Alumnos[self.__cantidad] = unAlumno
        self.__cantidad +=1
        
    
    def testAlumnos(self):
        archivo = open('alumnos.csv')
        reader=csv.reader(archivo,delimiter=';')
        next(reader)
        
        for fila in reader:
            unAlumno = Alumno.Alumno(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.agregaAlumno(unAlumno)
        
        archivo.close()
    
    def mostrarInforme(self,nota,fecha,dni):
        i = 0
        ban = False
        while ban == False and i < self.__cantidad:
            if self.__Alumnos[i].Alumno.getDNI == dni:
                ban = True
            else:
                i +=1
            
        nom = self.__Alumnos[i].Alumno.getNombre()
        apell = self.__Alumnos[i].Alumno.getApeliido()
        año = self.__Alumnos[i].Alumnno.getAño()
        print('{:10}{:5},{:5}{:10}{:10}{:10}\n\n'.format(dni,apell,nom,fecha,nota,año))
        
    
    def listado(self):
        primero = []
        segundo = []
        tercero = []
        cuarto = []
        quinto = []
        for i in range(self.__cantidad):
            if self.__Alumnos[i].getAño() == 1:
                primero.append(self.__Alumnos[i])
            elif self.__Alumnos[i].getAño() == 2:
                segundo.append(self.__Alumnos[i])
            elif self.__Alumnos[i].getAño() == 3:
                tercero.append(self.__Alumnos[i])
            elif self.__Alumnos[i].getAño() == 4:
                cuarto.append(self.__Alumnos[i])
            else:
                quinto.append(self.__Alumnos[i])

        for i in range(len(primero)-1):
            min = i
            j=i+1
            for j in range(len(primero)):
                if primero[j].getApellido() <  primero[min].getApellido():
                    min = j
            
            aux = primero[i]
            primero[i]=primero[min]
            primero[min]=aux
        
        
        for i in range(len(primero)):
            print(primero[i])
            
        for i in range(len(segundo)):
            print(segundo[i])
        
        for i in range(len(tercero)):
            print(tercero[i])
        
        for i in range(len(cuarto)):
            print(cuarto[i])
        
        for i in range(len(quinto)):
            print(quinto[i])
                
                    
                    
                
    
        

            
            
