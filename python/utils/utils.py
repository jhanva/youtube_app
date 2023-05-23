from transformers import pipeline


# Cargamos el modelo pre-entrenado de Sentiment Analysis
sentiment_classifier = pipeline("sentiment-analysis")


def clasificador_sentimientos(df, columna_comentarios):
    # Crear una nueva columna en el DataFrame para almacenar los resultados del análisis de sentimiento
    df['sentimiento'] = None
    df['score'] = None

    # Iterar sobre cada fila del DataFrame y aplicar el clasificador de sentimientos a los comentarios
    for index, row in df.iterrows():
        comentario = row[columna_comentarios]
        resultado = sentiment_classifier(comentario)[0]
        df.at[index, 'sentimiento'] = resultado['label']
        df.at[index, 'score'] = resultado['score']

    return df