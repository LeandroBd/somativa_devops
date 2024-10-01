from fastapi import FastAPI

app = FastAPI()


@app.get("/teste3")
async def root():
    return {"message": "SOMATIVA DEU CERTOOOOOOOOOOOOOOOO"}

@app.get("/teste4")
async def funcaoteste():
    return {"teste": True, "UHUUUUUUUUULLLLLLLLLLLLLL  ":}
