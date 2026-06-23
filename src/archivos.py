'''
modulo dedicado a la lectura/escritura de archivos 

'''

ARCHIVO = 'drug_side_effects_10k.csv'

def tupla_a_dict(titulo : tuple, linea : tuple) -> dict:

    '''
    funcion auxiliar de archivo_a_dict()

    dado el titulo y las linea procesadas a tuplas
    devuelve un diccionario donde a cada titulo le corresponde su respectivo valor

    ejemplo:

      titulo : (edad, genero, pais)
      contenido : (18,femenino,Arg)

    retorno: 

        {edad:18,genero:femenino,pais:Arg}

    solo maneja casos individuales, debe iterarse con un for
    
    '''

    diccionario_linea = {}

    for i in range(min(len(titulo),len(linea))): # min compara dos numeros y devuelve el menor

        diccionario_linea.update({titulo[i] : linea[i]})

    return diccionario_linea

def linea_a_tupla(linea :str):

    '''
    convierte cada linea del dataset en una tupla
    ejemplo:

        "edad,nombre,enfermedad\n" -> (edad, nombre, enfermedad)
    
    '''
    
    return tuple(linea.replace('\n','').split(','))

def archivo_a_dict(archivo : str) -> list[dict]:
    '''
    esta funcion es la encargada de leer el archivo csv

    - obtiene los titulos de los dataset y su contenido

    - devuelve una lista de diccionarios donde la clave corresponde al titulo y
      el valor corresponde al valor puntual del caso

      retorno: 

        [{edad:18,genero:femenino,pais:Arg}, {edad:70,genero:masculino,pais:Francia}]

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

dataset = archivo_a_dict(ARCHIVO)


if __name__ == '__main__': # esto es para imprimir la estructura de datos solo para este modulo y poder hacer pruebas

    print(dataset)

print(dataset)  