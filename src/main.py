from fastapi import FastAPI
from interfaces.api.url_shortener import router as url_shortener_router
from interfaces.api.url_redirect import router as redirect

app = FastAPI()

app.include_router(url_shortener_router,prefix="/api/v1")
app.include_router(redirect)


@app.get("/")
async def root():
    return {"status": "API Principal Funcionando OK"}