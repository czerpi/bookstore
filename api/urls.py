from django.urls import path

from api import views


urlpatterns = [
    path("books/", views.BooksViewSet.as_view()),
]
