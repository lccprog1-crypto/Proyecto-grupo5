import archivos

def test_tupla_a_dict():

    titulo_test = ('campo 1','campo 2','campo 3')
    tupla_test = ('dato 1','dato 2','dato 3')

    retorno = {'campo 1': 'dato 1',
                'campo 2':'dato 2',
                'campo 3':'dato 3'}

    # cuando titulo y contenido tienen la misma cantidad de elementos
    assert archivos.tupla_a_dict(titulo_test,tupla_test) == retorno

    titulo_test_2 = ('campo 1','campo 2','campo 3','valor extra')

    # cuando titulo tiene un elemento extra respecto a contenido
    assert archivos.tupla_a_dict(titulo_test_2,tupla_test) == retorno

    tupla2 = ('dato 1','dato 2','dato 3','valor extra')

    # cuando contenido tiene un elemento extra respecto a titulo
    assert archivos.tupla_a_dict(titulo_test,tupla2) == retorno
    

    
def test_linea_a_tupla():

    assert archivos.linea_a_tupla('edad,nombre,enfermedad\n') == ('edad','nombre','enfermedad')
    assert archivos.linea_a_tupla('') == ('',)