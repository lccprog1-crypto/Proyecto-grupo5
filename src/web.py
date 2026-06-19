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


def crear_grafica_lineas(ejex : list | tuple,ejey : list|tuple):


    fig,ax = mpl.subplots()
    ax.plot(ejex,ejey)

    st.pyplot(fig)


def crear_selector(opciones : tuple | list,etiqueta: str =''):

    seleccion = st.selectbox(label=etiqueta,
                 options=opciones)
    
    st.write(f'se muestran resultados para: {seleccion}')

    return seleccion


def listar_paises_drogas():

    drogas = []
    paises = utilidades.listar_elementos(etiqueta='country')

    for pais in paises:

        droga,_ =utilidades.droga_mas_impacto(pais)

        drogas.append(droga)

       
    return paises,drogas


def efecto_segun_medicamento(droga : str) -> list:

    '''
    toma como valor el nombre de una droga y retona dos listas, esta funcion se usa para pasarle los
    valores a la grafica

    primer retorno: lista de sintomas de la droga

    segundo retorno: lista de casos con esos sintomas

    
    '''

    sintomas = []
    cantidades = []

    lista_casos = utilidades.listar_sintomas_repeticion(droga)

    for sintoma, num in utilidades.contar_elementos_total(lista_casos):

        sintomas.append(sintoma)
        cantidades.append(num)

    return sintomas,cantidades

def desplegar_dashboard_droga_sintoma():

    lista_drogas = utilidades.listar_elementos(etiqueta='drug_name')
    seleccion = crear_selector(opciones=lista_drogas)
    
    if seleccion is not None:
        sintomas , cantidades = efecto_segun_medicamento(seleccion)
        crear_grafica_lineas(sintomas,cantidades)
    


def levantar_web():

    st.title('Trabajo Practico - Grupo 5')
    st.header(':blue[Tema:] efectos colaterales en medicamentos')

    
    desplegar_dashboard_droga_sintoma()


    enfermos_sanos,pais_droga= st.tabs(['Grafico enfermos vs sanos','Droga vs pais'])
    #   ESTO ES SOLO UN PROTOTIPO:
    #   TODO: MEJORAR PANEL Y HACERLO MAS LLAMATIVO
    total = utilidades.cantidad_afectados()

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
