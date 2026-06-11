'modulo que gestiona funciones utiles para el programador'
import archivos
import utilidades


def enfermedades_prev(linea : dict) -> bool:
    '''
    dada una linea en formato diccionario, devuelve un booleano indicando si el paciente
    tiene enfermedades previas
    
    '''

    return linea['chronic_condition'] != ''


def cantidad_afectados():

    '''
    lista-->int,int
    usaremos esta funcion para contar las personas que estaban afectadas anteriormente por alguna enfermedad
    
    '''
    data = archivos.archivo_a_lista_tupla(archivos.ARCHIVO)
    enfermos=0
    sanos=0

    for linea in data:

        if enfermedades_prev(linea):
            enfermos+=1
        else:
            sanos+=1

    total=(enfermos,sanos)
    return total


def porcentaje():
    enfermo, sano = cantidad_afectados()
    total=enfermo+sano
    porcentaje_sano = round(((sano / total) * 100),2)
    porcentaje_enfermo=round(((enfermo/total)*100),2)
    return porcentaje_sano,porcentaje_enfermo 

print(porcentaje())

