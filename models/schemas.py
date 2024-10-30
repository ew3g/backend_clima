from pydantic import BaseModel
from typing import Optional

class PrevisaoResponse(BaseModel):
    data: str
    probabilidade_evento_atipico: float
    is_temperatura_abaixo_media: Optional[bool]
    temperatura_abaixo_media_obtida: Optional[float]
    temperatura_minima_media: Optional[float]
    is_temperatura_acima_media: Optional[bool]
    temperatura_acima_media_obtida: Optional[float] 
    temperatura_maxima_media: Optional[float]
    is_precipitacao_acima_media: Optional[bool]
    precipitacao_acima_media_obtida: Optional[float]
    precipitacao_media: Optional[float]
    is_vento_acima_media: Optional[bool]
    vento_acima_media_obtido: Optional[float]
    vento_media: Optional[float]
    media_utilizada: Optional[str]