from fastapi import FastAPI

app = FastAPI()


@app.get("/teste3")
async def root():
    return {"message": "Hello World"}

@app.get("/teste4")
async def funcaoteste():
    return {"teste": "Teste ok"}