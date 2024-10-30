import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('database/clima.db')
    cursor = conn.cursor()
    cursor.execute(
        # '''
        # CREATE TABLE IF NOT EXISTS previsoes (
        #     data TEXT PRIMARY KEY,
        #     probabilidade_evento REAL,
        #     is_temp_abaixo_media BOOLEAN,
        #     temp_abaixo_media_medida REAL,
        #     temp_min_media REAL,
        #     is_temp_acima_media BOOLEAN,
        #     temp_acima_media_medida REAL,
        #     temp_max_media REAL,
        #     is_precipitacao_acima_media BOOLEAN,
        #     precipitacao_acima_media_medida REAL,
        #     precipitacao_media REAL,
        #     is_vento_acima_media BOOLEAN,
        #     vento_acima_media_medido REAL,
        #     vento_medio REAL,
        #     descricao TEXT
        # )
        # '''
        '''
        CREATE TABLE IF NOT EXISTS previsoes (
            data TEXT PRIMARY KEY,
            probabilidade_evento_atipico REAL,
            is_temperatura_abaixo_media BOOLEAN,
            temperatura_abaixo_media_obtida REAL,
            temperatura_minima_media REAL,
            is_temperatura_acima_media BOOLEAN,
            temperatura_acima_media_obtida REAL,
            temperatura_maxima_media REAL,
            is_precipitacao_acima_media BOOLEAN,
            precipitacao_acima_media_obtida REAL,
            precipitacao_media REAL,
            is_vento_acima_media BOOLEAN,
            vento_acima_media_obtido REAL,
            vento_media REAL,
            media_utilizada TEXT
        )
        '''
    )
    df = pd.read_csv('data/tabela-previsao-dados-extremos.csv')
    df.to_sql('previsoes', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

init_db()