from rest_framework import serializers
from rest_framework import status
from base.models import User, Profile
from utils.exceptions import CustomException
from utils.caching import CachingProcedureHandler
from utils.constants import Constants


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


class LoginRequestSerializer(serializers.Serializer):
    """ Serializer for login request data """
    email = serializers.CharField()

    def validate(self, attrs):

        users = User.objects.filter(email=attrs["email"])
        if not users.exists():
            raise CustomException(
                "user with this email does not exists",
                "email",
                status.HTTP_401_UNAUTHORIZED
            )

        return super().validate(attrs)
    
    def send_token(self):
        """ generates token, store in the cache and sent it via email """
        cache_handler = CachingProcedureHandler()
        token = cache_handler.generate_token()
        result = cache_handler.set_key(
            Constants.LOGIN_CACHE_TYPE,
            self.data["email"],
            token
        )
        if not result:
            raise CustomException(
                "Failed to store token in cache",
                "caching",
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        print("Stored in cache...")
