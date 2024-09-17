from fastapi import FastAPI

app = FastAPI()


@app.get("/teste3")
async def root():
    return {"message": "Hello World"}

@app.get("/teste4")
async def funcaoteste():
<<<<<<< HEAD
    return {"teste": True, "Num_aleatório ": random.randint(0, 50000)}
=======
    return {"teste": "Teste ok"}
>>>>>>> cf8907c4b5ca25571b5df6a49b32284de4dbca21
