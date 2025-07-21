from django.urls import path
from rest_framework.routers import DefaultRouter

import api.views as views

router = DefaultRouter()
router.register("category", views.CategoryModelViewSet)

urlpatterns = [
                  path("books/list", views.books_list),
                  path("books/create/", views.books_create),
                  path("books/detail/<int:pk>", views.books_detail),
                  path("books/update/<int:pk>", views.books_update),
                  path("books/delete/<int:pk>", views.books_delete),
              ] + router.urls
