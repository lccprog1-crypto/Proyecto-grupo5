'modulo que gestiona funciones utiles para el programador'


def enfermedades_prev(linea : tuple) -> bool:
    '''
    esta funcion toma una linea del dataset y devuelve un bool si 
    la persona tiene enfermedades base 
    
    '''

    return linea[11] != ''
