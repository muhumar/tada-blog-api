import datetime

from starlette.requests import Request


async def setup_logging(request: Request, call_next):
    log_entry = {
        "date_time": datetime.datetime.now().isoformat(),
        "method": request.method,
        "url": request.url.path,
    }

    print(log_entry)

    response = await call_next(request)
    return response
