from fastapi import Request, status
from fastapi.responses import JSONResponse

from blog_api.exceptions import (ArticleAlreadyExists, ArticleNotFound,
                                 ArticleValidationError)
from blog_api.routes import app


@app.exception_handler(ArticleNotFound)
async def article_not_found_exception_handler(request: Request, exc: ArticleNotFound):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(ArticleAlreadyExists)
async def article_already_exists_exception_handler(
    request: Request, exc: ArticleAlreadyExists
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)}
    )


@app.exception_handler(ArticleValidationError)
async def validation_error_exception_handler(
    request: Request, exc: ArticleValidationError
):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": exc.args[0]},
    )
