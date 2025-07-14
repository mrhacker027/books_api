from rest_framework import serializers

import main.models as models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        # fields = ("id", "name", "author", "added_at")
        exclude = ("description",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        return data


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        return data
