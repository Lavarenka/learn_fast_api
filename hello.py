from fastapi import FastAPI, Body, Header

app = FastAPI()


@app.post("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
    # reload перезапустить сервер если садержимое изменится
