'modulo para el muestreo web'

import streamlit as st
import matplotlib.pyplot as mpl
import utilidades

def grafico_torta(datos : list|tuple,etiquetas : list = None,formato = None):

    fig,ax = mpl.subplots()
    ax.pie(datos,labels=etiquetas,autopct=formato)
    st.pyplot(fig)


def crear_grafico_barras(ejex : list | tuple,ejey : list | tuple,titulo :str = '',titulox : str = '',tituloy : str = ''):

    fig,ax = mpl.subplots()

    ax.bar(ejex,
           ejey)
    
    ax.set_ylabel(tituloy)
    ax.set_xlabel(titulox)

    st.pyplot(fig)


def listar_paises_drogas():

    drogas = []
    paises = utilidades.listar_paises()

    for pais in paises:

        droga,_ =utilidades.droga_mas_impacto(pais)

        drogas.append(droga)

       
    return paises,drogas


def levantar_web():

    st.title('Trabajo Practico - Grupo 5')
    st.header(':blue[Tema:] efectos colaterales en medicamentos')

    total = utilidades.cantidad_afectados()


    enfermos_sanos,pais_droga= st.tabs(['Grafico enfermos vs sanos','Droga vs pais'])
    #   ESTO ES SOLO UN PROTOTIPO:
    #   TODO: MEJORAR PANEL Y HACERLO MAS LLAMATIVO

    with enfermos_sanos:

        st.write('Este grafico muestra el porcentaje de personas sanas y con enfermedades base que sufren efectos colaterales')

        grafico_torta(total,
                        ['personas con enfermedades base','personas sanas'],
                        formato='%1.2f%%')
        

    with pais_droga:
        
        st.write('Droga con mayor efecto colateral segun el pais')
        
        paises, drogas = listar_paises_drogas()
        crear_grafico_barras(paises,
                            drogas,
                            )

