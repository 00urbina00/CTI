from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Proyecto": "Control de Tráfico Inteligente"}