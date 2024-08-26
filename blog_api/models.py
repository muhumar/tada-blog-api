from typing import List, Optional, ClassVar

from pydantic import BaseModel, ValidationError

from blog_api.exceptions import (
    ArticleAlreadyExists,
    ArticleNotFound,
    ArticleValidationError
)


class Article(BaseModel):
    id: int
    title: str
    content: str

    _articles: ClassVar[List['Article']] = []

    @classmethod
    def get_articles(cls) -> List['Article']:
        return cls._articles

    @classmethod
    def get_article_by_id(cls, article_id: int) -> Optional['Article']:
        try:
            return next(article for article in cls._articles if article.id == article_id)
        except StopIteration:
            raise ArticleNotFound(article_id)

    @classmethod
    def add_article(cls, article_data: dict) -> 'Article':
        try:
            article = cls(**article_data)
        except ValidationError as e:
            raise ArticleValidationError(e.errors())


        if next((article for article in cls._articles if article.id == article.id), None):
            raise ArticleAlreadyExists(article.id)

        cls._articles.append(article)
        return article

    @classmethod
    def remove_article(cls, article_id: int) -> bool:
        article = cls.get_article_by_id(article_id)
        cls._articles.remove(article)
