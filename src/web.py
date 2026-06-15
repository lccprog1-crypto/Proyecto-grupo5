'modulo para el muestreo web'

import streamlit as st
import matplotlib.pyplot as mpl
import utilidades

def grafico_torta(datos : list|tuple,etiquetas : list = None,formato = None):

    fig,ax = mpl.subplots()
    ax.pie(datos,labels=etiquetas,autopct=formato)
    st.pyplot(fig)





def levantar_web():

    st.title('Trabajo Practico - Grupo 5')
    st.header(':blue[Tema:] efectos colaterales en medicamentos')

    st.write('Este grafico muestra el porcentaje de personas sanas y con enfermedades base que sufren efectos colaterales')
    total = utilidades.cantidad_afectados()
    grafico_torta(total,
                  ['personas con enfermedades base','personas sanas'],
                  formato='%1.2f%%')
    
    
    # dado un pais ¿cual es el medicamento con mas efectos colaterales?
    
