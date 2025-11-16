from fastapi import FastAPI
from app.auth.routes import router as auth_router

app = FastAPI(title="DaaS Backend", version="1.0.0")

# Include routers
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "DaaS Backend API is running!"}