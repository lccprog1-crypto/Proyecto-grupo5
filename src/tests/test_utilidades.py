import utilidades
import archivos



def test_enfermedades_prev():

    titulo_test = ('edad','genero','pais','chronic_condition') # chronic_condition debe coincidir porque busca este campo si o si, los demas pueden ser cualquiera
    tupla_test = ('41', 'Female', 'Germany','Kidney Disease')
    tupla_test2 = ('28', 'Male', 'USA', '' )

    dict_test = archivos.tupla_a_dict(titulo_test,tupla_test)
    dict_test2 = archivos.tupla_a_dict(titulo_test,tupla_test2)
    
    
    assert utilidades.enfermedades_prev(dict_test) is True  # tiene enfermedades
    assert utilidades.enfermedades_prev(dict_test2) is False # no tiene