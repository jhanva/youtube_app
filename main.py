from python.youtube.youtube import comentarios_youtube
from python.utils.utils import clasificador_sentimientos
from python.utils.utils import get_video_id


if __name__ == '__main__':

    url = input('Ingresa url de youtube: ')
    
    video_id = get_video_id(url)
    max_results = 100

    df = comentarios_youtube(video_id, max_results)
    df = clasificador_sentimientos(df, 'comentarios')

    print(df.head())