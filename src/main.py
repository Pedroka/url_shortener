from fastapi import FastAPI
from interfaces.api.url_shortener import router as url_shortener_router
from interfaces.api.url_searcher import router as url_search_router

app = FastAPI()

app.include_router(url_shortener_router,prefix="/api/v1")


@app.get("/")
async def root():
    return {"status": "API Principal Funcionando OK"}