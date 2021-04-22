import pytest

from django.db.utils import IntegrityError
from api.models import Book, Author, Tag


@pytest.mark.django_db
def test_tag_model_create():
    name = "tag"
    Tag.objects.create(name=name)
    tags = Tag.objects.all()
    assert tags.exists() is True
    assert tags.count() == 1
    tag = tags.first()
    assert tag.name == name


@pytest.mark.django_db
def test_tag_model_create_check_unique_name():
    name = "tag"
    Tag.objects.create(name=name)
    with pytest.raises(IntegrityError):
        Tag.objects.create(name=name)


@pytest.mark.django_db
def test_author_model_create():
    name = "Author"
    Author.objects.create(name=name)
    authors = Author.objects.all()
    assert authors.exists() is True
    assert authors.count() == 1
    author = authors.first()
    assert author.name == name


@pytest.mark.django_db
def test_author_model_create_check_unique_name():
    name = "Author"
    Author.objects.create(name=name)
    with pytest.raises(IntegrityError):
        Author.objects.create(name=name)


@pytest.mark.django_db
def test_book_model_create(author):
    name = "Book"
    Book.objects.create(
        name=name,
        author=author,
    )

    books = Book.objects.all()
    assert books.exists() is True
    assert books.count() == 1
    book = books.first()
    assert book.name == name
    assert book.author_id == author.id


@pytest.mark.django_db
def test_book_model_create_check_unique_name(author):
    name = "Book"
    Book.objects.create(
        name=name,
        author=author,
    )
    with pytest.raises(IntegrityError):
        Book.objects.create(
            name=name,
            author=author,
        )


@pytest.mark.django_db
def test_book_model_create_with_tags(author, tag_1, tag_2):
    name = "Book"
    book = Book.objects.create(
        name=name,
        author=author,
    )
    book.tags.add(tag_1, tag_2)
    book.save()
    book_db = Book.objects.filter(name=name).first()
    assert book == book_db
    assert book.tags.all().count() == 2
    assert list(book.tags.all()) == [tag_1, tag_2]


@pytest.mark.django_db
def test_book_model_create_without_author():
    name = "Book"
    with pytest.raises(IntegrityError):
        Book.objects.create(name=name)
