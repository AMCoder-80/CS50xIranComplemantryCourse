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
    BMI = serializers.FloatField(read_only=True)
    user = UserCreationSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = (
            "age", "weight", "heigth",
            "avatar", "description", "BMI", "user"
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
        user = self.context['user']
        weight = self.validated_data['weight']
        heigth = self.validated_data['heigth']
        BMI = round(weight / (heigth / 100)**2, 1)
        profile = Profile.objects.create(
            user=user,
            BMI=BMI,
            **validated_data
        )
        print(profile)
        return profile