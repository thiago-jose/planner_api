import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from database.connection import Settings
from routes.users import user_router
from routes.events import event_router


settings = Settings()
app = FastAPI()

# Register routes
app.include_router(user_router,  prefix="/user")
app.include_router(event_router, prefix="/event")

# register origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':

    # Note: Host must be "0.0.0.0" for Docker port forward to work
    uvicorn.run("main:app", host="0.0.0.0", port=8080,
                reload=True)
