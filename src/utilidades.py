'modulo que gestiona funciones utiles para el programador'
import archivos


def eliminar_repeticiones_lista(lista : list) -> list:
    '''
    data una lista crea una copia de la misma quitando elementos repetidos

    ejemplo:

    eliminar_repeticiones_lista([1,1,2,3]) -> [1,2,3]

    '''

    copia = []

    for elemento in lista:

        if elemento not in copia:

            copia.append(elemento)
    
    return copia



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

def calcular_porcentaje(valor: int,total : int) -> float:  # IMPORTANTE: es pobable que sea eliminada

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

def contar_elementos_total(lista : list) -> list[tuple[str,int]]:
    '''
    a diferencia de contar_elementos_repetidos() el cual retorna el elemento
    con el mayor numero de casos, contar_elementos_total() retorna una lista de tuplas 
    con el elemento y su cantidad repeticiones de forma individual.

    ejemplo:

        contar_elementos_total(['vomitos','vomitos','nauseas']) -> [('vomitos',2),('nauseas',1)]

    '''

    conteos = []

    for elemento in eliminar_repeticiones_lista(lista):

        n = lista.count(elemento)

        conteos.append((str(elemento),n))

    return conteos



def droga_mas_impacto(pais : str) -> tuple[str]:

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

def porcentaje_afectados(): # IMPORTANTE: es pobable que sea eliminada
    enfermo, sano = cantidad_afectados()
    total=enfermo+sano
    porcentaje_sano = calcular_porcentaje(sano,total)
    porcentaje_enfermo=calcular_porcentaje(enfermo,total)

    return porcentaje_sano,porcentaje_enfermo 



def listar_elementos(dataset : list[dict] = archivos.dataset,etiqueta : str = 'country',repetir : bool = False) -> list[str]:

    '''
    esta funcion recibe un argumento de tipo dataset (por defecto el archivo csv) y
    una etiqueta (por defecto 'country')

    etiqueta = clave del diccionario

    retorno: lista de valores del diccionario

    si repetir es True, repite elementos en la lista, de lo contrario solo lo incluye una vez

    por defecto repetir esta en False
    
    '''

    elementos = []

    for linea in dataset:

        el = linea.get(etiqueta)

        if el is None:

            el = ''


        if not repetir and not el in elementos:

            elementos.append(str(el)) # fuerza a que el elemento se transforme en un str
        

        if repetir : # incluye todos los elementos aunque esten repetidos
            elementos.append(str(el))

            

    return elementos


def listar_sintomas_repeticion(droga : str,dataset : list[dict] = archivos.dataset) -> list[str]:

    '''
    lista los sintomas dado el nombre de una droga

    IMPORTANTE:

    retorna una lista donde los elementos se pueden repetir a diferencia de
    listar_elementos() donde se descartan elementos repetidos
    
    '''

    lista_casos = []

    casos = clasificar_dataset(clave='drug_name',
                                clasificacion=droga,
                                dataset=dataset)
    

    for caso in casos:

        efecto = caso.get('side_effect')

        if efecto is not None:

            lista_casos.append(str(efecto))

    return lista_casos