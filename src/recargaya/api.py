from fastapi import FastAPI
from pydantic import BaseModel
from recargaya.recargas import calcular_recarga

app = FastAPI()

class RecargaRequest(BaseModel):
    monto: float
    premium: bool = False

@app.post("/calcular-recarga")
def calcular(data: RecargaRequest):
    resultado = calcular_recarga(data.monto, data.premium)
    return {
        "resultado": resultado
    }