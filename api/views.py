from rest_framework import serializers
from rest_framework.generics import ListAPIView

from api.models import Book
from api.serializers import BookSerializer, TagsRequestSerializer


class BooksViewSet(ListAPIView):
    serializer_class = BookSerializer
    request_serializer = TagsRequestSerializer
    """
        View to list books on request.
    """

    def get_queryset(self):
        qs = (
            Book.objects.all()
            .select_related(
                "author",
            )
            .prefetch_related(
                "tags",
            )
        )
        return qs

    def filter_queryset(self, queryset):
        request_serializer = TagsRequestSerializer(data=self.request.query_params)
        if not request_serializer.is_valid():
            raise serializers.ValidationError({"errors": request_serializer.errors})

        tags = request_serializer.data["tags"]
        tags = [x.strip() for x in tags.split(",")]
        queryset = queryset.filter(tags__name__in=tags)
        return queryset.distinct().order_by("name")
