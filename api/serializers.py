from rest_framework import serializers

import main.models as models


class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        return data


class BookSerializer(BaseSerializer):
    class Meta:
        model = models.Book
        exclude = ("description",)


class BookDetailSerializer(BaseSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class BookPostSerializer(BaseSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
