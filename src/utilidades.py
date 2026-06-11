'modulo que gestiona funciones utiles para el programador'
import archivos
import utilidades


def enfermedades_prev(linea : tuple) -> bool:
    '''
    esta funcion toma una linea del dataset y devuelve un bool si 
    la persona tiene enfermedades base 
    
    '''

    return linea[11] != ''


def cantidad_afectados():

    '''
    lista-->int,int
    usaremos esta funcion para contar las personas que estaban afectadas anteriormente por alguna enfermedad
    
    '''
    _,cuerpo=archivos.archivo_a_lista_tupla(archivos.ARCHIVO)
    enfermos=0
    sanos=0

    for tupla in cuerpo:

        if enfermedades_prev (tupla):
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
print (porcentaje())

