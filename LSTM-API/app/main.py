from fastapi import FastAPI
from model import predict 
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de dados para receber as features
class Features(BaseModel):
    features: List[float]

# Endpoint para previsões
@app.post("/predict/")
def get_prediction(features: Features):
    prediction = predict(features.features)  # Função predict carregará o modelo e fará a previsão
    return {'prediction': prediction}

@app.get("/metrics")
async def metrics():
    return generate_latest()

@app.get("/predict/")
async def get_prediction(features: list):
    prediction = predict(features)
    return {"prediction": prediction}


#Middleware Prometheus
app.middleware("http")(add_prometheus_metrics)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






