'modulo que gestiona funciones utiles para el programador'
import archivos


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
    data = archivos.archivo_a_dict(archivos.ARCHIVO)
    enfermos=0
    sanos=0

    for linea in data:

        if enfermedades_prev(linea):
            enfermos+=1
        else:
            sanos+=1

    total=(enfermos,sanos)
    return total

def calcular_porcentaje(valor: int,total : int) -> float: # TODO: hacer tests

    'dado un valor (conjunto acotado de un total) y un total, calcula su porcentaje'


    return round((valor/total) * 100,2)


def clasificar_dataset(clave : str, clasificacion :str, archivo : str= archivos.ARCHIVO) -> list[dict]:

    '''
    esta funcion devuelve una lista de diccionarios que cumplan con la clasificacion establecida

    ejemplo :

    -  clave: 'country'

    -  clasificacion: 'Pakistan'

    
    esto devuelve una lista de diccionarios que corresponden al pais de Pakistan unicamente

    si no hay coincidencias devuelve una lista vacia

    '''

    clasif = []

    for linea in archivos.archivo_a_dict(archivo):

        if linea.get(clave) == clasificacion:

            clasif.append(linea)
    
    return clasif



def porcentaje_afectados(): # TODO: documentar esta funcion
                            # TODO: modificarla para poder hacerle los tests
    enfermo, sano = cantidad_afectados()
    total=enfermo+sano
    porcentaje_sano = calcular_porcentaje(sano,total)
    porcentaje_enfermo=calcular_porcentaje(enfermo,total)

    return porcentaje_sano,porcentaje_enfermo 

print(porcentaje_afectados())

