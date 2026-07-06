'modulo para el muestreo web'

import streamlit as st
import matplotlib.pyplot as mpl
import utilidades
from archivos import dataset



# TODO: documentar las funciones de este modulo
# TODO: diseñar mas preguntas dinamicas

def grafico_torta(datos : list,etiquetas : list = None,formato = None):

    fig,ax = mpl.subplots()
    ax.pie(datos,labels=etiquetas,autopct=formato)
    st.pyplot(fig)


def crear_grafico_barras(ejex : list,ejey : list ,titulo :str = '',titulox : str = '',tituloy : str = '',tamañox = 10,tamañoy = 10):

    fig,ax = mpl.subplots()

    ax.bar(ejex,
           ejey)
    
    ax.set_ylabel(tituloy)
    ax.set_xlabel(titulox)
    fig.set_size_inches(tamañox,tamañoy)

    st.pyplot(fig)


def crear_grafica_lineas(ejex : list ,ejey : list,titulox : str = '',tituloy : str = '',tamañox = 10,tamañoy = 10):


    fig,ax = mpl.subplots()
    ax.plot(ejex,ejey)
    ax.set_xlabel(titulox.capitalize())
    ax.set_ylabel(tituloy.capitalize())
    fig.set_size_inches(tamañox,tamañoy)

    st.pyplot(fig)


def crear_selector(opciones : list,etiqueta: str =''):

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

    lista_casos = utilidades.listar_sintomas_repeticion(droga)
    sintomas,cantidades = utilidades.agrupar_elementos_tupla(utilidades.contar_elementos_total(lista_casos))

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

    drogas,cantidades = utilidades.agrupar_elementos_tupla(listado_drogas_cantidad)

    crear_grafico_barras(ejex = drogas,
                            ejey = cantidades,
                            titulox = 'droga con mas efectos secundarios',
                            tituloy = 'numero de casos',
                            tamañox = 15,
                            tamañoy = 10
                        )

def droga_mas_efectos():

    '''
    cuenta la cantidad de repeticiones de droga en el dataset y retorna una lista
    con la droga y otra lista con la cantidad de casos para posteriormente llevas a cabo la grafica
    
    '''


    lista_drogas_repetidas = utilidades.listar_elementos(etiqueta='drug_name',
                                                        repetir=True)
    
    # esto lo que hace es agrupar en las drogas con el resto de drogas
    # agrupar los valores de cantidades con los valores de cantidades
    # el primer elemento de la lista drogas esta relacionado con el primer elemento
    # de la lista de repeticiones y asi sucesivamente

    totales_elementos = utilidades.contar_elementos_total(lista_drogas_repetidas)

    drogas,repeticiones_drogas = utilidades.agrupar_elementos_tupla(totales_elementos)
    
    
    return drogas,repeticiones_drogas


def listar_franja_etaria(dataset : list[dict] = dataset) -> dict:
    """
    promedia la edad de las personas que tiene efectos adversos en cada pais,
    
    retorna dos listas: la primera corresponde a paises y la segunda corresponde a el valor numerico

    """

    
    promedios_etarios = []

    paises = utilidades.listar_elementos(dataset=dataset) # lista los paises sin repeticiones a partir del dataset que se le pase
    # no le paso todos los argumentos porque no es necesario, ya tiene los argumentos que necesito por defecto
    
    for pais in paises:

        dataset_pais = utilidades.clasificar_dataset(dataset=dataset,clave='country',clasificacion=pais)

        edades_pais = utilidades.listar_elementos(dataset=dataset_pais,
                                       etiqueta='age',
                                       repetir=True)
        
        promedio_etario = int(utilidades.promedio_lista(edades_pais)) # dado que es un promedio de edad
                                                    # busco la parte entera

        promedios_etarios.append(promedio_etario)
        

    
    return paises, promedios_etarios



def ranking_paises():
    st.subheader('Ranking de paises con mas casos de efectos colaterales')


    paises = utilidades.listar_elementos() # por defecto va a tomar el dataset del archivo, y la key country 
                                           # es por eso que no le paso ningun parametro: no es necesario

    paises_casos = [] # lista que almacenara la cantidad de casos y el pais en formato de tupla

    for pais in paises:

        numero_casos = utilidades.cantidad_efectos_colaterales(pais)

        paises_casos.append((numero_casos,pais))


    # Lista de coordenadas para el mapa (Latitud y Longitud)
    # sacadas de internet busque el centro de cada pais del top


    coordenadas_mapa = []

    for pais in paises:

        lat,long = utilidades.localizar_pais(pais)

        coordenadas_mapa.append({'lat':lat,'long':long})

    
    # divide la pantalla en 2 para mostrar el mapa  y el top
    columna_izquierda, columna_derecha = st.columns([2, 1])

    with columna_izquierda:
        st.markdown("Mapa de casos por país")
        st.map(coordenadas_mapa, size=40,latitude='lat',longitude='long')

    with columna_derecha:

        cant_paises = len(paises)

        st.markdown('Top ' + str(cant_paises) + ' Países')

        for puesto in range(1,cant_paises + 1): # TODO: ver de abstraer esta logica de ordenamiento haciendo una funcion
                
            top = max(paises_casos)
            cantidad = top[0]
            nombre_pais = top[1]
        
            st.write("puesto", puesto, "-", nombre_pais, ":", cantidad, "casos")

            paises_casos.remove(top)
    


def levantar_web():

    st.title('Proyecto de Programación II - Grupo 5')
    st.header('Tema: efectos colaterales en medicamentos')
    st.header('Integrantes:\n Fiori Santino, Urbaneja Matias, Rojas Lucca',divider=True)
              


    # PREGUNTA NRO 7 (DINAMICA):
    desplegar_dashboard_droga_sintoma()  # pregunta que responde: dado un medicamento ¿que efectos colaterales puede provocar?


    enfermos_sanos,pais_droga,med_mas_doc, top_ranking,prom_et = st.tabs([
                                        'Grafico enfermos vs sanos',
                                        'Droga vs pais',
                                        'medicamentos mas documentados',
                                        'ranking de paises',
                                        'grafico de promedios etarios'])
    
    # pregunta que responde: dado un pais ¿que medicamento tiene el mayor impacto?

    st.header('Grafico droga con mas efectos secundarios por pais')
    desplegar_dashboard_pais_droga()
    

    total = utilidades.cantidad_afectados()


    # seccion para preguntas estaticas

    # PREGUNTA NOR 5 (ESTATICA):
    with enfermos_sanos: # pregunta que responde : ¿que porcentaje de la poblacion es suceptible a efectos adversos?

        st.header('Este grafico muestra el porcentaje de personas sanas y con enfermedades base que sufren efectos colaterales')

        grafico_torta(total,
                        ['personas con enfermedades base','personas sanas'],
                        formato='%1.2f%%')
        
        
                      # PREGUNTA NRO 8 (ESTATICA):
    with pais_droga:  # pregunta que responde: dado un pais ¿que medicamento tiene el mayor impacto?
        
        st.header('Droga con mayor efecto colateral segun el pais')
        
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

                          # PREGUNTA NRO 1 (ESTATICA):
    with top_ranking: # pregunta que responde: ¿cuales son los paises con mas casos de efectos colaterales?
        st.write('Ranking de paises con mas casos de efectos colaterales')
        ranking_paises()

    with prom_et: # PREGUNTA NRO 2 (ESTATICA)

        paises, rango_et = listar_franja_etaria()
        st.header('En esta grafica se muestra el promedio de edad de las personas que sufren efectos colaterales segun el pais')

        crear_grafica_lineas(ejex=paises,
                             ejey=rango_et,
                             titulox='Pais',
                             tituloy='Rangos etarios promedios')


def main():

    levantar_web()

if __name__ == '__main__':

    main()