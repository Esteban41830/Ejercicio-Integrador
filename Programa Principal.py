import ManejadorMedicamento
import ManejadorCama


if __name__ == '__name__':
    
    manejaCam = ManejadorCama.ManjadorCama()
    manejaMed = ManejadorMedicamento.ManejadorMedicamento()
    manejaCam.AgregarCama()
    manejaMed.AgregarMedicamento()
    
    print('------------------------Buscar Paciente------------------------')
    Apellido = input('Apellido del paciente: ')
    Nombre = input('Nombre del paciente: ')
    manejaCam.BuscarPaciente(Nombre,Apellido)
    
    print('------------------------Buscar por Diagnostico------------------')
    diagnostico = input('Ingrese diagnostico: ')
    manejaCam.ListadoPaciete(diagnostico)