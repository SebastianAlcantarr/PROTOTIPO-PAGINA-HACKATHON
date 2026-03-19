from pydantic import BaseModel
from typing import Optional



class InversionParametros(BaseModel):
    sector: str
    presupuesto_min: float
    presupuesto_max: float
    plazo_retorno: str
    riesgo: str
    preferencias: Optional[str] = None

class EmpresaSugerida(BaseModel):
    nombre: str
    sector: str
    quienes_son: Optional[str] = None
    origen: Optional[str] = None
    por_que_encaja: str
    nivel_riesgo: str
    potencial_retorno: str

class RespuestaInversion(BaseModel):
    empresas: list[EmpresaSugerida]
    resumen: str