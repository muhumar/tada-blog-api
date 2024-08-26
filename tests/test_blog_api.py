from fastapi.testclient import TestClient

from blog_api.routes import app

client = TestClient(app)


def test_get_articles_initially_empty():
    response = client.get("/articles/")
    assert response.status_code == 200
    assert response.json() == []


def test_add_articles():
    response = client.post(
        "/articles/", json={"id": 1, "title": "Test", "content": "Content"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "Test", "content": "Content"}


def test_get_articles_after_add():
    response = client.get("/articles/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_article():
    response = client.get("/articles/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test", "content": "Content"}


def test_get_non_existent_article():
    response = client.get("/articles/999/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Article with ID 999 not found."}


def test_delete_article():
    response = client.delete("/articles/1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Article removed"}


def test_delete_non_existent_article():
    response = client.delete("/articles/999/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Article with ID 999 not found."}
