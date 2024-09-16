from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "Num_aleatório: ": random.randint(0, 5000)}