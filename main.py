from fastapi import FastAPI, HTTPException
from models.schemas import PrevisaoResponse
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = getattr(sys, '_MEIPASS', os.path.abspath("."))
DB_PATH = os.path.join(BASE_DIR, "database", "clima.db")
DATA_DIR = os.path.join(BASE_DIR, "data")

app = FastAPI(openapi_url="/openapi.json")

# Configurações de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://localhost:4200/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectar ao banco SQLite
def get_db_connection():
    # conn = sqlite3.connect('database/clima.db')
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Previsão

# GET http://localhost:8000/previsao/31_12
@app.get("/previsao/{dia_mes}", response_model=PrevisaoResponse)
async def get_previsao(dia_mes: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM previsoes WHERE data LIKE ?", (f'%{dia_mes}',))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Previsão não encontrada")
    
    return dict(row)

# http://localhost:8000/listar-dias-eventos
@app.get("/listar-dias-eventos")
async def listar_dias_eventos():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT distinct data FROM previsoes")
    rows = cursor.fetchall()
    conn.close()

    datas = [row["data"] for row in rows]

    return datas



# Gráficos

# Tendência anual temperatura
# http://localhost:8000/grafico-tendencia-temperatura/2020
@app.get("/grafico-tendencia-temperatura/{ano}")
async def grafico_tendencia_temperatura(ano: int):
    #file_path = f"data/graficos/tendencia_anual_temperatura/tendencia_anual_temperatura_{ano}.png"
    file_path = os.path.join(DATA_DIR, "graficos", "tendencia_anual_temperatura", f"tendencia_anual_temperatura_{ano}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")

# Tendência anual precipitação
# http://localhost:8000/grafico-tendencia-precipitacao-anual/2020
@app.get("/grafico-tendencia-precipitacao-anual/{ano}")
async def grafico_tendencia_precipitacao_anual(ano: int):
    # file_path = f"data/graficos/tendencia_anual_precipitacao/ano/tendencia_anual_precipitacao_{ano}.png"

    file_path = os.path.join(DATA_DIR, "graficos", "tendencia_anual_precipitacao", "ano", f"tendencia_anual_precipitacao_{ano}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")

@app.get("/grafico-tendencia-precipitacao-geral")
# http://localhost:8000/grafico-tendencia-precipitacao-geral
async def grafico_tendencia_precipitacao_geral():
    # file_path = f"data/graficos/tendencia_anual_precipitacao/geral/tendencia_anual_precipitacao.png"

    file_path = os.path.join(DATA_DIR, "graficos", "tendencia_anual_precipitacao", "geral", "tendencia_anual_precipitacao.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")

# Médias temperaturas
# http://localhost:8000/grafico-medias-temperaturas/2020
@app.get("/grafico-medias-temperaturas/{ano}")
async def grafico_medias_temperaturas(ano: int):
    # file_path = f"data/graficos/medias_temperaturas/temperaturas_{ano}.png"

    file_path = os.path.join(DATA_DIR, "graficos", "medias_temperaturas", f"temperaturas_{ano}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")

# Rosa dos ventos
# http://localhost:8000/grafico-rosa-ventos
@app.get("/grafico-rosa-ventos")
async def grafico_rosa_ventos():
    # file_path = f"data/graficos/rosa_dos_ventos/rosa_dos_ventos.png"

    file_path = os.path.join(DATA_DIR, "graficos", "rosa_dos_ventos", "rosa_dos_ventos.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")

# Precipitação Mensal
# http://localhost:8000/grafico-precipitacao-mensal/2020
@app.get("/grafico-precipitacao-mensal/{ano}")
async def grafico_precipitacao_mensal(ano: int):
    # file_path = f"data/graficos/precipitacao_mensal/precipitacao_mensal_{ano}.png"

    file_path = os.path.join(DATA_DIR, "graficos", "precipitacao_mensal", f"precipitacao_mensal_{ano}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Gráfico não encontrado")
    
    return FileResponse(file_path, media_type="image/png")