from rest_framework import serializers
from rest_framework import status
from base.models import User, Profile
from utils.exceptions import CustomException
from utils.caching import CachingProcedureHandler
from utils.constants import Constants
from utils.email import EmailHandler


class UserCreationSerializer(serializers.ModelSerializer):
    """ Create user serializer """
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email"
        )
  
    def run_validation(self, data=...):
        print("Validating................")
        users = User.objects.filter(email=data['email'])
        if users:
            raise CustomException(
                "this email is already registered",
                "error",
                status.HTTP_400_BAD_REQUEST
            )
        return data


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
                "error",
                status.HTTP_406_NOT_ACCEPTABLE
            )
        
        user = self.context['user']
        profiles = Profile.objects.filter(user=user)
        if profiles.exists():
            raise CustomException(
                "Your already have a profile",
                "error",
                status.HTTP_400_BAD_REQUEST
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


class VerifyTokenSerializer(serializers.Serializer):
    """ Get token from user and validate it """
    token = serializers.CharField()

    def validate(self, attrs):
        """ Validate user token """
        cache_handler = CachingProcedureHandler()
        token = attrs['token']
        email = cache_handler.get_key(Constants.LOGIN_CACHE_TYPE, token)
        if email is None:
            raise CustomException(
                "Invalid token",
                "error",
                status.HTTP_403_FORBIDDEN
            )
        attrs.update({
            "email": email
        })
        return attrs

    def get_user(self):
        email = self.validated_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise CustomException(
                "requested user does not exists",
                "error",
                status.HTTP_400_BAD_REQUEST
            )
        return user


class LoginRequestSerializer(serializers.Serializer):
    """ Serializer for login request data """
    email = serializers.EmailField()

    def validate(self, attrs):

        users = User.objects.filter(email=attrs["email"])
        if not users.exists():
            raise CustomException(
                "user with this email does not exists",
                "error",
                status.HTTP_401_UNAUTHORIZED
            )

        return super().validate(attrs)
    
    def send_token(self):
        """ generates token, store in the cache and sent it via email """
        cache_handler = CachingProcedureHandler()
        email_handler = EmailHandler()
        email = self.data["email"]
        token = cache_handler.generate_token()
        result = cache_handler.set_key(
            Constants.LOGIN_CACHE_TYPE,
            email,
            token
        )
        if not result:
            raise CustomException(
                "Failed to store token in cache",
                "error",
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        email_handler.send_otp(email, token)


class GetUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def run_validation(self, data=...):
        return data
        

class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = GetUserDataSerializer()

    class Meta:
        model = Profile
        fields = ['age', 'weight', 'heigth', 'description', 'avatar', 'BMI', 'user']
        read_only_fields = ['BMI', 'avatar'] 

    def update(self, instance, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user', None)
        
        for attr, value in validated_data.items():
            if value:
                setattr(instance, attr, value)
        instance.save()

        print(user_data is None)
        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        return instance
