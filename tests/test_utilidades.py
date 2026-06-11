import src.utilidades as utilidades

def test_enfermedades_prev():

    tupla_test = ('PT-174479', '41', 'Female', 'Germany', 'Insulin', '10', 'Hypoglycemia', 'Moderate', 'Recovered', '2025-02-18', '2025-01-24', 'Kidney Disease', 'No', 'Frequent', 'No', '38.0', '52.52', '13.405')
    tupla_test2 = ('PT-101653', '28', 'Male', 'USA', 'Metformin', '5', 'Diarrhea', 'Moderate', 'Recovered', '2024-01-05', '2023-11-13', '', 'Yes', '', 'No', '42.0', '38.9072', '-77.0369')
    assert utilidades.enfermedades_prev(tupla_test) is True  # tiene enfermedades
    assert utilidades.enfermedades_prev(tupla_test2) is False # no tiene