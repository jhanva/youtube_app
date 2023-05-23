# External libraries
import pandas as pd

from googleapiclient.discovery import build

# Own libraries
from python.utils.read_files import read_yaml
from python.metadata.path import Path


data = read_yaml(Path.credentials)
api_key = data['api_key']
youtube = build('youtube', 'v3', developerKey=api_key)


def comentarios_youtube(video_id, max_results):

    comments = []
    next_page_token = ''

    while True:
        # Realizamos la búsqueda de comentarios utilizando la API de YouTube
        results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=max_results,
            pageToken=next_page_token
        ).execute()

        # Recorremos los resultados y extraemos los datos de cada comentario
        for result in results.get('items', []):
            # Obtenemos el texto del comentario
            comment = result['snippet']['topLevelComment']['snippet']['textDisplay']
            
            # Agregamos el comentario a la lista
            comments.append(comment)

        # Verificamos si hay más resultados disponibles
        if 'nextPageToken' in results:
            next_page_token = results['nextPageToken']
        else:
            break

    df = pd.DataFrame({'comentarios': comments})

    return df