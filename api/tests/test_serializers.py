import pytest

from api.serializers import BookSerializer, TagsRequestSerializer


def test_tags_serialize_fields():
    fields_to_check = {"tags"}
    assert fields_to_check == TagsRequestSerializer().fields.keys()


def test_tags_serializer_valid():
    data = {"tags": "novel,crime,drama"}
    serializer = TagsRequestSerializer(data=data)
    assert serializer.is_valid()
    tags = serializer.data["tags"]
    assert tags
    assert data["tags"] == tags


def test_tags_serializer_valid():
    data = {"tags": 34}
    serializer = TagsRequestSerializer(data=data)
    assert serializer.is_valid()
    tags = serializer.data["tags"]
    assert tags
    assert str(data["tags"]) == tags


def test_tags_serializer_not_valid_empty_string():
    data = {"tags": ""}
    serializer = TagsRequestSerializer(data=data)
    assert serializer.is_valid() is False


def test_tags_serializer_not_valid_empty_string():
    serializer = TagsRequestSerializer(data={})
    assert serializer.is_valid() is False


def test_book_serializer_fields():
    fields_to_check = {"name", "author", "tags"}
    assert fields_to_check == BookSerializer().fields.keys()


@pytest.mark.django_db
def test_book_serializer_output(minimal_book, author):
    serializer = BookSerializer(instance=minimal_book)
    assert serializer.data
    assert serializer.data.keys() == {"author", "name", "tags"}
    assert serializer.data["author"] == author.name
    assert serializer.data["name"] == minimal_book.name
    assert serializer.data["tags"] == ""


@pytest.mark.django_db
def test_book_serializer_output_with_tags(minimal_book, author, tag_1, tag_2):
    minimal_book.tags.add(tag_1)
    minimal_book.tags.add(tag_2)
    minimal_book.save()

    serializer = BookSerializer(instance=minimal_book)
    assert serializer.data
    assert serializer.data.keys() == {"author", "name", "tags"}
    assert serializer.data["author"] == author.name
    assert serializer.data["name"] == minimal_book.name
    assert serializer.data["tags"] == f"{tag_1.name},{tag_2.name}"
