from django.urls import path

import api.views as views

urlpatterns = [
    path("books/list", views.books_list),
    path("books/create/", views.books_create),
    path("books/detail/<int:pk>", views.books_detail),
    path("books/update/<int:pk>", views.books_update),
    path("books/delete/<int:pk>", views.books_delete),
]
