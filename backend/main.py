from contextlib import asynccontextmanager

from fastapi import FastAPI
from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # helper lifespan, creating table 
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
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
