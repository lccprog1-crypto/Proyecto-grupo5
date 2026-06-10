'''
modulo dedicado a la lectura/escritura de archivos 

'''

ARCHIVO = 'drug_side_effects_10k.csv'


def archivo_a_lista_tupla(archivo : str) -> list[tuple]:
    '''
    recibe un archivo y devuelve dos valores:
    primer valor : una tupla con la primer linea del archivo (debe corresponder con el titulo del dataset)
    segundo valor: corresponde al cuerpo del dataset (informacion conformada por una lista de tuplas)

    primer retorno:

    titulo -> (tupla)

    segundo retorno:
    
    cuerpo -> [(tupla1),(tupla2), ...] lista de tuplas

    '''

    data = []
    
    with open(archivo,'r') as doc: 

        for linea in doc:
            
            linea_tupla = tuple(linea.replace('\n','').split(','))
            # reeplazo el salto de linea por un string vacio,
            # convierto el string a lista dividierdo por el caracter ","
            data.append(linea_tupla) # añado el conjunto de datos a la lista

    titulo = data[0]
    cuerpo = data[1:]
        
    return titulo, cuerpo


# TODO: diseñar mecanismo para extraer cada campo para categorizarlo de forma limpia y ordenada