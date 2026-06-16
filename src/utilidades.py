'modulo que gestiona funciones utiles para el programador'
import archivos

def enfermedades_prev(linea : dict) -> bool:
    '''
    dada una linea en formato diccionario, devuelve un booleano indicando si el paciente
    tiene enfermedades previas
    
    '''
    condicion_cronica = linea.get('chronic_condition')

    return  condicion_cronica is not None and condicion_cronica != ''


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


def clasificar_dataset(clave : str, clasificacion :str,dataset : list[dict] = archivos.dataset) -> list[dict]:

    '''
    esta funcion devuelve una lista de diccionarios que cumplan con la clasificacion establecida

    ejemplo :

    -  clave: 'country'

    -  clasificacion: 'Pakistan'

    
    esto devuelve una lista de diccionarios que corresponden al pais de Pakistan unicamente

    si no hay coincidencias devuelve una lista vacia

    '''

    clasif = []

    for linea in dataset:

        if linea.get(clave) == clasificacion:

            clasif.append(linea)
    
    return clasif


def contar_elementos_repetidos(lista : list) -> tuple[str,int]:

    '''
    funcion que dada una lista devuelve el elemento mas repetido
    y el numero de veces de dicha repeticion
    
    
    '''


    anterior = 0
    elemento_anterior = ''

    for elemento in set(lista):

        n = lista.count(elemento)

        if n > anterior:
            
            anterior = n
            elemento_anterior = str(elemento)
    
    return elemento_anterior,anterior



def droga_mas_impacto(pais : str) -> list[str]:

    '''
    dado un pais devuelve la droga que mas efectos colaterales tiene en dicho pais
    junto con el numero de casos

    ejemplo :

    droga_mas_impacto('India') -> (Ibuprofeno,30) 
    
    es decir que la droga con mas efectos colaterales en India es el Ibuprofeno con 30 casos documentados

    '''


    clasif = clasificar_dataset(clave='country',clasificacion=pais)
    listado = []

    for linea in clasif:
        listado.append(linea.get('drug_name'))

    return contar_elementos_repetidos(listado)

def porcentaje_afectados(): # TODO: documentar esta funcion
                            # TODO: modificarla para poder hacerle los tests
    enfermo, sano = cantidad_afectados()
    total=enfermo+sano
    porcentaje_sano = calcular_porcentaje(sano,total)
    porcentaje_enfermo=calcular_porcentaje(enfermo,total)

    return porcentaje_sano,porcentaje_enfermo 

