"""
Entrypoint for the backend (FastAPI)
"""
import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from backend.config import LOGGER, SETTINGS
from backend.database import DATABASE
from backend.routers import frontend, slack, spotify, users
from backend.worker import worker_entrypoint


APP = FastAPI()

# Temporary hack to allow access to the cookie within the frontend
APP.add_middleware(SessionMiddleware, secret_key=SETTINGS.sss_secret_key)
APP.error_middleware.app.security_flags = "samesite=lax"  # type:ignore

APP.mount(
    frontend.STATIC_FILES_PATH,
    frontend.STATIC_FILES_APP,
    name=frontend.STATIC_FILES_NAME,
)

APP.include_router(frontend.ROUTER)
APP.include_router(slack.ROUTER)
APP.include_router(spotify.ROUTER)
APP.include_router(users.ROUTER)


@APP.on_event("startup")
async def startup():
    """
    Startup actions
    """
    loop = asyncio.get_running_loop()
    await loop.create_task(DATABASE.connect())
    loop.create_task(worker_entrypoint())


@APP.on_event("shutdown")
async def shutdown():
    """
    Shutdown actions
    """
    # pylint:disable=import-outside-toplevel
    current_task = asyncio.current_task()
    other_tasks = [t for t in asyncio.all_tasks() if t is not current_task]
    LOGGER.info("Cancelling %s outstanding tasks", len(other_tasks))
    for task in other_tasks:
        task.cancel()

    await DATABASE.disconnect()
    await asyncio.gather(*other_tasks, return_exceptions=True)


if __name__ == "__main__":
    logging.basicConfig(level=2, format="%(levelname)-9s %(message)s")
    CONFIG = uvicorn.Config(
        APP,
        host="0.0.0.0",
        port=SETTINGS.port,
        lifespan="on",
        loop="asyncio",
        log_level="info",
        use_colors=True,
        workers=1,
    )
    SERVER = uvicorn.Server(config=CONFIG)

    LOOP = asyncio.new_event_loop()
    asyncio.set_event_loop(LOOP)

    try:
        LOOP.run_until_complete(SERVER.serve())
    except asyncio.CancelledError:
        pass
