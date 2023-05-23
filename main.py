from python.youtube.youtube import comentarios_youtube
from python.utils.utils import clasificador_sentimientos


if __name__ == '__main__':
    
    video_id = 'RSjF0PwU1FA' 
    max_results = 100

    df = comentarios_youtube(video_id, max_results)
    df = clasificador_sentimientos(df, 'comentarios')

    print(df.head)