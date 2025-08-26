from fastapi import FastAPI

app = FastAPI()

@app.get("/ping", tags=["Teste"])
def test():
    return {"messase": "Pong"}

