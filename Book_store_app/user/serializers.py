from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class used in DRF to convert objcet into bytes
    """

    def create(self, validated_data):
        """
        built in method for the serializer class to craete the db
        """
        return User.objects.create_user(**validated_data)
        

    class Meta:
        """
        meta class is used to change the behaviour of the model
        fields 
        """
        model = User
        fields = ['id', 'username', 'password',
                  'email', 'phone_number', 'location']
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}