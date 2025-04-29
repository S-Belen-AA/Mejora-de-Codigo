
import requests

from dotenv import load_dotenv

import os

# Cargar variables de entorno

def cargar_variables_entorno():

    load_dotenv()

    api_key = os.getenv("API_KEY_SEARCH_GOOGLE")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    
    return api_key, search_engine_id

# Construcción de la URL para la API de Google Custom Search

def construir_url(
        
    api_key,
    search_engine_id,
    query='filetype:sql "MySQL dump" (pass|password|passwd|pwd)',
    page=1,
    lang="lang_es"
):
    return f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

# Realizar solicitud a la API 

def realizar_solicitud(url):

    try:

        # Hacer solicitud

        response = requests.get(url)

        # Convertir a JSON (a diccionario de PYTHON)

        data = response.json()

        #Devolver los datos

        return data

# En caso de errores

    except requests.exceptions.RequestException as e: # "RequestException" es una clase que representa errores de conexión (como sin internet, mala URL, etc). 

        # Error de red

        print("Ocurrió un error al hacer la solicitud")

        return None # Aclaración tardía, "return" es una "keyword" en python que nos sirve para devolver un valor desde una función al lugar donde fue llamada.
                    # "None" Es un valor especial que significa “nada”, “vacío” o “no hubo resultado”.

# Aquí obtendremos los datos que solicitamos

def mostrar_resultados(datos):
     
    resultados = datos.get('items', {}) # "items" es una clave del diccionario principal "datos" que contiene una lista de diccionarios.

    if not resultados:

        print("No se encontraron resultados.")

    else:

        # Determinaremos que si no se encuentra un valor específico, no devuelva "None" sino que un "texto alternativo".

        for item in resultados: # Aquí con "item"recorremos la lista de diccionarios dentro de "items"

            title = item.get('title', 'Título no disponible')

            link = item.get('link', 'Link no disponible')

            snippet = item.get('snippet', 'Descripción no disponible')

    print(f"Title: {title}")

    print(f"Link: {link}")

    print(f"Snippet: {snippet}")

    print("-" * 80)

if __name__ == "__main__":

    print("Resultados:")

    api_key, search_engine_id = cargar_variables_entorno()

    mi_url = construir_url(api_key, search_engine_id)

    datos = realizar_solicitud(mi_url)

    if datos:
        mostrar_resultados(datos)