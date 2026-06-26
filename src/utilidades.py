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


def cantidad_afectados() -> tuple[int,int]:

    '''
    lleva un conteo de las personas enfermas (personas con enfermedades base)
    y sanas (personas sin enfermedades base)

    retorna una tupla con las personas que tienen enfermedades base y las que no 
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

    retorno -> tupla donde el primer elemento es un string y el segundo un int

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
    
    retorna una lista de sintomas donde dichos sintomas pueden repetirse
    '''

   
    casos = clasificar_dataset(clave='drug_name',
                                clasificacion=droga,
                                dataset=dataset)
    

    lista_casos = listar_elementos(dataset=casos,etiqueta='side_effect',repetir=True)

    return lista_casos

def listar_drogas_repeticion_pais(pais :str): 

    '''
    esta funcion admite un pais y retorna una lista de tuplas con las drogas 

    y las cantidades de casos de que de las mismas

    ejemplo:

    listar_drogas_repeticion_pais('Pakistan') -> [(Ibuprofen,10),(Insulin,5), ...]
    
    
    '''


    dataset_filtrado = clasificar_dataset(clave='country',clasificacion=pais)

    

    drogas_repetidas = listar_elementos(etiqueta='drug_name',
                                        repetir=True,
                                        dataset=dataset_filtrado)
 
    
    return contar_elementos_total(drogas_repetidas)


def agrupar_elementos_tupla(lista : list[tuple]):

    '''
    esta funcion recibe una lista de tuplas de dos elementos

    y agrupa dichos elementos en dos listas separadas que luego son retornadas

    esta funcion se utiliza para preparar los datos para pasar a graficar
    
    ejemplo:

        agrupar_elementos_tupla([(vomito,2),(fiebre, 4)]) -> ([vomito,fiebre] , [2,4])

    ACLARACION: si la tupla tiene un tamaño distinto de 2 es ignorada
 
    '''

    agrupacion_A = []
    agrupacion_B = []


    for tupla in lista:

        if len(tupla) == 2:

            agrupacion_A.append(tupla[0])
            agrupacion_B.append(tupla[1])

    return agrupacion_A,agrupacion_B


def efectos_colaterales(linea : dict) -> bool:
    '''
    dada una linea en formato diccionario, devuelve un booleano indicando si el paciente
    tiene efectos colaterales 
    
    '''
    efecto_colateral = linea.get('side_effect')

    return  efecto_colateral is not None and efecto_colateral != ''


def cantidad_efectos_colaterales(pais, dataset = archivos.dataset) -> int: 

    '''
    lleva un conteo de las personas con efectos colaterales 
    retorna un int con la cantidad de personas con efectos colaterales 
    '''
    
    con_efectos = 0

    for linea in dataset: # si el dataset no se ása como argumento pasa el dataset del csv

        # filtra el dataset por pais y si tiene efectos colaterales,
        #  si cumple ambas condiciones suma 1 a con_efectos
        if linea.get("country") == pais and efectos_colaterales(linea):
            con_efectos+=1

    
    return con_efectos


def localizar_pais(pais : str,dataset : list[dict] = archivos.dataset) -> tuple[float,float]:

    '''
    dado un pais, retorna una tupla de flotantes con las coordenadas de dicho pais

    ejemplo:

    localizar_pais('India') -> (20.5937,78.9629) 

    el primer valor es latitud y el segundo valor es longitud
    
    '''

    i = 0  # i es un contador que va incrementando de uno en uno (indice)

    # esto podria resolverse con un bucle for y al encontrar un elemento retornar el valor inmediatamente
    # opte por hacerlo de esta forma para evitar hacer un return dentro del for

    while i < len(dataset):

        elemento = dataset[i]

        if elemento.get('country') == pais:

            
            lat = elemento.get('capital_lat')
            long = elemento.get('capital_lon')

            if lat is None or long is None: # si no encuentra la key de longitud o latitud devuelve 0,0
                lat = 0.00
                long = 0.00

            coords = (float(lat),float(long))
            break # como ya encontre el valor que buscaba rompo el while

        i+= 1

    return coords







