from rest_framework import serializers
from .models import Book
from user.models import User




class AllBookListSerializer(serializers.ModelSerializer):
    """
    serializer class for getting all the book
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'quantity']


class BookSerializer(serializers.ModelSerializer):
    """
        serializer class for creating all the book
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    def validate(self, attrs):
        user=attrs.get("user")
        if not user.is_superuser:
            raise serializers.ValidationError("unautherized access")
        return super().validate(attrs)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'quantity','user']
        required_field = ['title', 'author', 'price', 'quantity','user']


    def create(self, validated_data):

        validated_data.pop("user")
        print(validated_data)
        return self.Meta.model.objects.create(**validated_data)