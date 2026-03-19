from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import InversionParametros,RespuestaInversion
from groc import analizar_oportunidades  # si la carpeta se llama 'backend' en minúsculas
import uvicorn

app = FastAPI(title="Inversor Hermosillo API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/analizar", response_model=RespuestaInversion)
async def analizar(params: InversionParametros):
    if not params.sector or not params.sector.strip():
        raise HTTPException(
            status_code=422,
            detail="El sector es obligatorio"
        )

    if params.presupuesto_min > params.presupuesto_max:
        raise HTTPException(
            status_code=422,
            detail="presupuesto_min no puede ser mayor que presupuesto_max"
        )

    try:
        resultado = analizar_oportunidades(params)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"status": "ok", "mensaje": "API activa"}
