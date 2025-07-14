from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import main.models as models
import api.serializers as serializers


@api_view(["GET"])
def books_list(request):
    books = models.Book.objects.all()
    serializer = serializers.BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def books_detail(request, pk):
    book = models.Book.objects.get(pk=pk)
    serializer = serializers.BookDetailSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)
