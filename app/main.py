from fastapi import FastAPI

app = FastAPI(title="Project UAV DaaS Geospasial", version="0.1.0")

@app.get("/")
def read_root():
    """
    Endpoint Gerbang Utama
    """
    return {"messsage" : "Yo, Gerbang API udah kebuka nih bang!"}