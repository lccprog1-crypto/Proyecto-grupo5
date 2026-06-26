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


dataset_test = [
                    {'country':'Argentina','drug_name':'...','smoker':'no','side_effect':'Pain'},
                    {'country':'Alemania','drug_name':'...','smoker':'yes','side_effect':'Headache','capital_lon':10.4515,'capital_lat':51.1657},
                    {'country':'Francia','drug_name':'...','smoker':'yes','side_effect':'Pain'},
                    {'country':'Colombia','drug_name':'...','smoker':'no','side_effect':'stomachache'},
                    {'country':'Argentina','drug_name':'...','smoker':'yes','side_effect':'Pain'},
                    {'country':'Alemania','drug_name':'test','smoker':'no','side_effect':'stomachache'}
                    
                    ]

def test_listar_elementos():

    
    
    assert utilidades.listar_elementos(dataset_test) == ['Argentina','Alemania','Francia','Colombia']
    assert utilidades.listar_elementos([]) == []
    assert utilidades.listar_elementos([],repetir=True) == []
    assert utilidades.listar_elementos(dataset_test,repetir=True) == ['Argentina','Alemania','Francia',
                                                                      'Colombia','Argentina','Alemania']
    
    assert utilidades.listar_elementos(dataset=dataset_test,
                                       etiqueta='testing') == [''] # caso donde la etiqueta que se introduce no existe

    assert utilidades.listar_elementos(dataset=dataset_test,
                                       etiqueta='testing'
                                       ,repetir=True) == [''] * len(dataset_test)

def test_listar_sintomas_repeticion():

    assert utilidades.listar_sintomas_repeticion(droga='...',dataset=dataset_test) == ['Pain','Headache','Pain','stomachache','Pain']
    assert utilidades.listar_sintomas_repeticion(droga='test',dataset=dataset_test) == ['stomachache']
    assert utilidades.listar_sintomas_repeticion(droga='...',dataset=[]) == []

def test_contar_elementos_total():

    assert utilidades.contar_elementos_total(['vomitos','vomitos','nauseas']) == [('vomitos',2),('nauseas',1)]
    assert utilidades.contar_elementos_total([]) == []

def test_eliminar_repeticiones_lista():

    assert utilidades.eliminar_repeticiones_lista([1,1,2,3]) == [1,2,3]

    assert utilidades.eliminar_repeticiones_lista([]) == []

def test_agrupar_elementos_tupla():

    assert utilidades.agrupar_elementos_tupla([('vomito',2),('fiebre', 4)]) == (['vomito','fiebre'],[2,4])

    assert utilidades.agrupar_elementos_tupla([]) == ([],[])
    
    # en caso de valor incorrecto
    assert utilidades.agrupar_elementos_tupla([('vomito',2),('fiebre', 4),('tos',2,3)]) == (['vomito','fiebre'],[2,4])

def test_localizar_pais():

    assert utilidades.localizar_pais(dataset=dataset_test,pais='Argentina') == (0.00,0.00) # caso donde existe el pais pero no encuentra las coordenadas
    assert utilidades.localizar_pais(dataset=dataset_test,pais='Alemania') == (51.1657,10.4515) # caso donde si lo encuentra
    # no importa si Alemania esta repetido en este caso, va a tomar el primer valor del dataset que coincida con Alemania
    assert utilidades.localizar_pais(dataset=dataset_test,pais='test') == (0.00,0.00) # caso que no existe