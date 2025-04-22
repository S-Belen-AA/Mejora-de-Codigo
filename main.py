
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
    return f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"

# Realizar la solicitud a la API

def realizar_solicitud(url):

response = requests.get(url)

data = response.json()



result= data.get('items', [])

if not result:

    print("No se encontraron resultados.")

else:

    for item in result:

        title = item.get('title')

        link = item.get('link')

        snippet = item.get('snippet')

        print(f"Title: {title}")

        print(f"Link: {link}")

        print(f"Snippet: {snippet}")

        print("-" * 80)

        