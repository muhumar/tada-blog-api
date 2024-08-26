from typing import List

from fastapi import FastAPI, Request, status

from blog_api.models import Article

app = FastAPI()

@app.get("/articles/", response_model=List[Article])
async def get_articles():
    return Article.get_articles()

@app.get("/articles/{article_id}/", response_model=Article)
async def get_articles(article_id: int):
    return Article.get_article_by_id(article_id)

@app.post("/articles/", response_model=Article, status_code=status.HTTP_201_CREATED)
async def add_article(request: Request):
    data = await request.json()
    return Article.add_article(data)

@app.delete("/articles/{article_id}/")
async def delete_article(article_id: int):
    Article.remove_article(article_id)
    return {"message": "Article removed"}
