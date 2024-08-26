import asyncio

import uvicorn

from blog_api.exception_handlers import *
from blog_api.logging_middleware import setup_logging
from blog_api.routes import app

app.middleware("http")(setup_logging)

def run():
    if not asyncio.get_event_loop().is_running():
        uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__=="__main__":
    run()
