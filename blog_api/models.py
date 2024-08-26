from typing import ClassVar, List, Optional

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
            cls.get_article_by_id(article.id)
            raise ArticleAlreadyExists(article.id)
        except ValidationError as e:
            raise ArticleValidationError(e.errors())
        except ArticleNotFound:
            pass

        cls._articles.append(article)
        return article

    @classmethod
    def remove_article(cls, article_id: int) -> bool:
        article = cls.get_article_by_id(article_id)
        cls._articles.remove(article)
