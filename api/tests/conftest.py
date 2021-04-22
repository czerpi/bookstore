import pytest

from api.models import Book, Tag, Author


@pytest.fixture
def tag_1():
    return Tag.objects.create(name='Tag 1')


@pytest.fixture
def tag_2():
    return Tag.objects.create(name='Tag 2')


@pytest.fixture
def author():
    return Author.objects.create(name='Author 1')


@pytest.fixture
def minimal_book(author):
    return Book.objects.create(
        name='Minimal book',
        author=author,
    )

