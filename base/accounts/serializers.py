from rest_framework import serializers
from rest_framework import status
from base.models import User, Profile
from utils.exceptions import CustomException


class UserCreationSerializer(serializers.ModelSerializer):
    """ Create user serializer """
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email"
        )


class ProfileCreationSerializer(serializers.ModelSerializer):
    """ Create user profile serializer """
    class Meta:
        model = Profile
        fields = (
            "age", "weight", "heigth",
            "avatar", "description",
        )
    
    def validate(self, attrs):

        if attrs["age"] < 18:
            raise CustomException(
                "Your age must be at least 18",
                "age",
                status.HTTP_406_NOT_ACCEPTABLE
            )
        return super().validate(attrs)

    def create(self, validated_data):
        print("Creating....")
        print(validated_data)