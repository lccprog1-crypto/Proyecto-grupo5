import archivos

def test_tupla_a_dict():

    titulo_test = ('campo 1','campo 2','campo 3')
    tupla_test = ('dato 1','dato 2','dato 3')

    assert archivos.tupla_a_dict(titulo_test,tupla_test) == {'campo 1': 'dato 1',
                                                             'campo 2':'dato 2',
                                                             'campo 3':'dato 3'}