import pytest
import json
import json

from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_api_response_not_valid():
    client = APIClient()
    response = client.get("/api/books/")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "errors" in response.data


@pytest.mark.django_db
def test_api_response_empty_response(tag_1, tag_2):
    client = APIClient()
    response = client.get("/api/books/?", data={"tags": f"{tag_1.name},{tag_2.name}"})
    assert response.status_code == status.HTTP_200_OK
    res = json.loads(response.content)
    assert res == []


@pytest.mark.django_db
def test_api_response(book, tag_1, tag_2, author):
    client = APIClient()
    response = client.get("/api/books/?", data={"tags": f"{tag_1.name},{tag_2.name}"})
    assert response.status_code == status.HTTP_200_OK
    res = json.loads(response.content)
    assert len(res) == 1
    assert res[0]["name"] == book.name
    assert res[0]["author"] == author.name
    assert res[0]["tags"] == f"{tag_1.name},{tag_2.name}"


@pytest.mark.django_db
def test_api_response_filtered(book, book_2, tag_1, tag_2):
    client = APIClient()
    response = client.get("/api/books/?", data={"tags": f"{tag_1.name},{tag_2.name}"})
    assert response.status_code == status.HTTP_200_OK
    res = json.loads(response.content)
    assert len(res) == 2
    assert res[0]["name"] == book.name
    assert res[1]["name"] == book_2.name


@pytest.mark.django_db
def test_api_response_filtered_one_result(book, book_2, tag_1, tag_2):
    client = APIClient()
    response = client.get("/api/books/?", data={"tags": f"{tag_2.name}"})
    assert response.status_code == status.HTTP_200_OK
    res = json.loads(response.content)
    assert len(res) == 1
    assert res[0]["name"] == book.name
    assert book_2.name not in res
