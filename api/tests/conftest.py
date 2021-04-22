import pytest

from api.models import Book, Tag, Author


@pytest.fixture
def tag_1():
    return Tag.objects.create(name="Tag 1")


@pytest.fixture
def tag_2():
    return Tag.objects.create(name="Tag 2")


@pytest.fixture
def author():
    return Author.objects.create(name="Author 1")


@pytest.fixture
def minimal_book(author):
    return Book.objects.create(
        name="Minimal book",
        author=author,
    )


@pytest.fixture
def book(minimal_book, author, tag_1, tag_2):
    book = minimal_book
    book.tags.add(tag_1)
    book.tags.add(tag_2)
    book.save()
    return book


@pytest.fixture
def book_2(author, tag_1):
    book = Book.objects.create(
        name="New book",
        author=author,
    )
    book.tags.add(tag_1)
    book.save()
    return book
