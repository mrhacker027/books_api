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


@api_view(["POST"])
def books_create(request):
    serializer = serializers.BookPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def books_update(request, pk):
    book = models.Book.objects.get(pk=pk)
    serializer = serializers.BookPostSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def books_delete(request, pk):
    book = models.Book.objects.get(pk=pk)
    book.delete()
    return Response({"message": "no content"}, status=status.HTTP_204_NO_CONTENT)
