import ManejadorAlumnos
import ManejadorMaterias

if __name__ == '__main__':
    
    ManejaA = ManejadorAlumnos.ManejaAlum()
    ManejaM = ManejadorMaterias.ManejaMaTeria()
    ManejaA.testAlumnos()
    ManejaM.testMaterias()
    
    print('Ingrese una de las siguientes opciones')
    opcion = ''
    while opcion != 's':
        opcion = input('a-Promedio con y sin aplazos\nb-Alumnos promocionales\nc-Listado\ns-Salir\n\n')
        
        if opcion == 'a':
            documento = int(input('DNI del alumno: '))
            ManejaM.promedio(documento)
            print('¿Que desea hacer ahora?\n')
            
        elif opcion == 'b':
            nombre = input('Ingrese el nombre de la materia: ')
            ManejaM.informe(nombre)     
            print('¿Que desea hacer ahora?\n')
        
        elif opcion == 'c':
            ManejaA.listado()
            print('¿Que desea hacer ahora?\n')
            
        elif opcion == 's':
            print('\n---------FIN DEL PROGRAMA----------\n')
            
        else:
            print('La opcion no es valida, ingrese nuevamente\n')