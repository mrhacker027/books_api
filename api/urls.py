from django.urls import path

import api.views as views

urlpatterns = [
    path("books/list", views.books_list),
    path("books/detail/<int:pk>", views.books_detail),
]
