import utilidades
import archivos

def test_clasificar_dataset():

    dataset_testing = [{'country':'Argentina','drug_name':'...','smoker':'yes'},
                       {'country':'Pakistan','drug_name':'...','smoker':'yes'},
                       {'country':'Poland','drug_name':'...','smoker':'no'}]

    assert utilidades.clasificar_dataset(clave='country',clasificacion='Argentina',dataset=dataset_testing) == [{'country':'Argentina','drug_name':'...','smoker':'yes'}]
    assert utilidades.clasificar_dataset(clave='drug_name',clasificacion='...',dataset=dataset_testing) == dataset_testing
    assert utilidades.clasificar_dataset(clave='testing',clasificacion='...',dataset=dataset_testing) == []



def test_enfermedades_prev():

    titulo_test = ('edad','genero','pais','chronic_condition') # para que se evalue la condicion
                                                               # debe existir el apartado de chronic_condition
                                                               # de lo contrario siempre da False
    titulo_test_2 = (('edad','genero','pais','id')) 
    tupla_test = ('41', 'Female', 'Germany','Kidney Disease')
    tupla_test2 = ('28', 'Male', 'USA', '' )

    dict_test = archivos.tupla_a_dict(titulo_test,tupla_test)
    dict_test2 = archivos.tupla_a_dict(titulo_test,tupla_test2)
    dict_test3 = archivos.tupla_a_dict(titulo_test_2,tupla_test2) 
    
    
    assert utilidades.enfermedades_prev(dict_test) is True  # tiene enfermedades
    assert utilidades.enfermedades_prev(dict_test2) is False # no tiene
    assert utilidades.enfermedades_prev(dict_test3) is False # este caso no tiene la seccion que se busca

def test_contar_elementos_repetidos():

    assert utilidades.contar_elementos_repetidos(['test','hola','mundo','test','test']) == ('test',3)
    assert utilidades.contar_elementos_repetidos([1,0,1,0,1,1,1]) == ('1',5)
    assert utilidades.contar_elementos_repetidos([]) == ('',0)


def test_calcular_porcentaje():

    assert utilidades.calcular_porcentaje(100, 1000) == 10
    assert utilidades.calcular_porcentaje(391, 1000) == 39.1
    assert utilidades.calcular_porcentaje(120, 210) == 57.14