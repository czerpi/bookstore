from rest_framework import serializers

from api.models import Book


class TagsRequestSerializer(serializers.Serializer):
    tags = serializers.CharField(
        allow_null=False,
        required=True,
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        fields = read_only_fields = "tags"


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=100, source="author.name")
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = read_only_fields = (
            "name",
            "author",
            "tags",
        )

    @staticmethod
    def get_tags(obj):
        return ",".join(obj.tags.values_list("name", flat=True))
