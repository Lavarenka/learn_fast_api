

from fastapi import FastAPI


from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router, )
app.include_router(users_router, )






@app.get("/hi")
def greet(who: str = "World"):  # World default value
    who = who.strip().title()
    return f"Hello? {who}?"







if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)  # hello - name file
    # reload перезапустить сервер если садержимое изменится
