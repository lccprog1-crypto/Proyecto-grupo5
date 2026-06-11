'''
modulo dedicado a la lectura/escritura de archivos 

'''

ARCHIVO = 'drug_side_effects_10k.csv'

def tupla_a_dict(titulo : tuple, linea : tuple):

    '''
    funcion auxiliar de linea_a_tupla()

    dado el titulo y las linea procesadas a tuplas
    devuelve un diccionario donde a cada titulo le corresponde su respectivo valor
    
    '''

    diccionario_linea = {}

    for i in range(len(titulo)):

        diccionario_linea.update({titulo[i] : linea[i]})

    return diccionario_linea

def linea_a_tupla(linea :str):

    '''
    convierte cada linea del dataset en una tupla
    ejemplo:

        "edad,nombre,enfermedad\n" -> (edad, nombre, enfermedad)
    
    '''
    
    return tuple(linea.replace('\n','').split(','))

def archivo_a_lista_tupla(archivo : str) -> list[dict]:
    '''
    recibe un archivo y devuelve dos valores:
    primer valor : una tupla con la primer linea del archivo (debe corresponder con el titulo del dataset)
    segundo valor: corresponde al cuerpo del dataset (informacion conformada por una lista de tuplas)

    primer retorno:

    titulo -> (tupla)

    segundo retorno:
    
    cuerpo -> [(tupla1),(tupla2), ...] lista de tuplas

    '''

    with open(archivo,'r') as doc: 

        titulo = linea_a_tupla(doc.readline())
        
        listado = []

        for linea in doc:
            
            linea_tupla = linea_a_tupla(linea)
            # reeplazo el salto de linea por un string vacio,
            # convierto el string a lista dividierdo por el caracter ","
            #lista_tupla.append(linea_tupla) # añado el conjunto de datos a la lista

            listado.append(tupla_a_dict(titulo,linea_tupla))
        
        return listado

# TODO: diseñar mecanismo para extraer cada campo para categorizarlo de forma limpia y ordenada

if __name__ == '__main__': # esto es para imprimir la estructura de datos solo para este modulo y poder hacer pruebas

    print(archivo_a_lista_tupla(ARCHIVO))

    