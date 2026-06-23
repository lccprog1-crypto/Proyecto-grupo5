'modulo para el muestreo web'

import streamlit as st
import matplotlib.pyplot as mpl
import utilidades


# TODO: documentar las funciones de este modulo
# TODO: diseñar mas preguntas dinamicas

def grafico_torta(datos : list|tuple,etiquetas : list = None,formato = None):

    fig,ax = mpl.subplots()
    ax.pie(datos,labels=etiquetas,autopct=formato)
    st.pyplot(fig)


def crear_grafico_barras(ejex : list | tuple,ejey : list | tuple,titulo :str = '',titulox : str = '',tituloy : str = '',tamañox = 10,tamañoy = 10):

    fig,ax = mpl.subplots()

    ax.bar(ejex,
           ejey)
    
    ax.set_ylabel(tituloy)
    ax.set_xlabel(titulox)
    fig.set_size_inches(tamañox,tamañoy)

    st.pyplot(fig)


def crear_grafica_lineas(ejex : list | tuple,ejey : list|tuple,titulox : str = '',tituloy : str = '',tamañox = 10,tamañoy = 10):


    fig,ax = mpl.subplots()
    ax.plot(ejex,ejey)
    ax.set_xlabel(titulox.capitalize())
    ax.set_ylabel(tituloy.capitalize())
    fig.set_size_inches(tamañox,tamañoy)

    st.pyplot(fig)


def crear_selector(opciones : tuple | list,etiqueta: str =''):

    seleccion = st.selectbox(label=etiqueta,
                 options=opciones)
    
    st.write(f'se muestran resultados para: {seleccion}')

    return seleccion


def listar_paises_drogas() -> tuple[list,list]:

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
    seleccion = crear_selector(opciones=lista_drogas,etiqueta='efectos colaterales mas comunes segun el medicamento')

    if seleccion is not None:

        sintomas , cantidades = efecto_segun_medicamento(seleccion)
        crear_grafica_lineas(sintomas,cantidades,
                             titulox='sintomas documentados',
                             tituloy='numero de casos documentados')
        
def desplegar_dashboard_pais_droga():

    '''
    esta funcion muestra el numero de casos por droga
    '''

    lista_paises = utilidades.listar_elementos(etiqueta = 'country')

    pais_seleccion = crear_selector(opciones=lista_paises,etiqueta='droga con mayor impacto segun el pais')

    # aclaracion : pais_seleccion es marcando como vacion None pero funciona bien

    listado_drogas_cantidad = utilidades.listar_drogas_repeticion_pais(pais_seleccion)

    drogas = []
    cantidades = [] # TODO:  ver si esta logica se puede abstraer

    for drog,cant in listado_drogas_cantidad:

        drogas.append(drog)
        
        cantidades.append(cant)

    
    crear_grafico_barras(ejex = drogas,
                            ejey = cantidades,
                            titulox = 'droga con mas efectos secundarios',
                            tituloy = 'numero de casos',
                            tamañox = 10,
                            tamañoy = 10
                        )

def droga_mas_efectos():

    '''
    cuenta la cantidad de repeticiones de droga en el dataset y retorna una lista
    con la droga y otra lista con la cantidad de casos para posteriormente llevas a cabo la grafica
    
    '''

    drogas = []
    repeticiones_drogas = []

    lista_drogas_repetidas = utilidades.listar_elementos(etiqueta='drug_name',
                                                        repetir=True)
    
    for droga,rep in utilidades.contar_elementos_total(lista_drogas_repetidas):

        drogas.append(droga)
        repeticiones_drogas.append(rep)

    return drogas, repeticiones_drogas


def levantar_web():

    st.title('Trabajo Practico - Grupo 5')
    st.header(':blue[Tema:] efectos colaterales en medicamentos')

    # PREGUNTA NRO 7 (DINAMICA):
    desplegar_dashboard_droga_sintoma()  # pregunta que responde: dado un medicamento ¿que efectos colaterales puede provocar?


    enfermos_sanos,pais_droga,med_mas_doc = st.tabs(['Grafico enfermos vs sanos',
                                        'Droga vs pais',
                                        'medicamentos mas documentados'])
    
# pregunta que responde: dado un pais ¿que medicamento tiene el mayor impacto?

    st.header('Grafico droga con mas efectos secundarios por pais')
    desplegar_dashboard_pais_droga()
    

    total = utilidades.cantidad_afectados()


    # seccion para preguntas estaticas

    # PREGUNTA NOR 5 (ESTATICA):
    with enfermos_sanos: # pregunta que responde : ¿que porcentaje de la poblacion es suceptible a efectos adversos?

        st.write('Este grafico muestra el porcentaje de personas sanas y con enfermedades base que sufren efectos colaterales')

        grafico_torta(total,
                        ['personas con enfermedades base','personas sanas'],
                        formato='%1.2f%%')
        
        
                      # PREGUNTA NRO 8 (ESTATICA):
    with pais_droga:  # pregunta que responde: dado un pais ¿que medicamento tiene el mayor impacto?
        
        st.write('Droga con mayor efecto colateral segun el pais')
        
        paises, drogas = listar_paises_drogas()
        crear_grafico_barras(paises,
                            drogas,
                            titulox='registro de paises',
                            tituloy='droga con mas impacto')
        

                      # PREGUNTA NRO 4 (ESTATICA):
    with med_mas_doc: # pregunta que responde: ¿cual es la droga con mayores casos de efectos colaterales?
                      # (a nivel mundial)
        med,casos = droga_mas_efectos()

        crear_grafica_lineas(med,casos,
                             tamañox=15,
                             titulox='medicamentos',
                             tituloy='numero de casos a escala mundial')


    