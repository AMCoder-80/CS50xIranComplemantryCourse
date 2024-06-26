# django related modules

# DRF related modules
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView

# Local modules
from base.accounts.serializers import (
    UserCreationSerializer, ProfileCreationSerializer,
    LoginRequestSerializer, VerifyTokenSerializer,
    ProfileUpdateSerializer
)
from base.models import User, Profile
from utils.auth import generate_jwt_for_user
from utils.exceptions import CustomException

# Third party modules


# @api_view(['POST'])
# def create_user(request):
#     """ Create new user """
#     if request.method == 'POST':
#         serialized = UserCreationSerializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.data, status=status.HTTP_200_OK)


# class UserCreationView(GenericAPIView):
#     """ Create new user instance """
#     serializer_class = UserCreationSerializer
#     queryset = User.objects.all()

#     def post(self, request, *args, **kwargs):
#         serialized = self.get_serializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         user = serialized.save()
#         tokens = RefreshToken.for_user(user)
#         update_last_login(None, user)
#         response = {
#             "refresh": str(tokens),
#             "access": str(tokens.access_token)
#         }
#         return Response(response, status=status.HTTP_201_CREATED)


class UserCreationView(GenericAPIView):
    """ Create new user instance """
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = serialized.save()
        response = generate_jwt_for_user(user)
        return Response(response, status=status.HTTP_201_CREATED)


class ProfileCreationView(CreateAPIView):
    """ Create new profile instance """
    serializer_class = ProfileCreationSerializer
    queryset = Profile

    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context["user"] = self.request.user
        return context
    

class LoginRequestView(GenericAPIView):
    """ User sends request to get OTP code """
    serializer_class = LoginRequestSerializer

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.send_token()
        return Response("Email sent", status=status.HTTP_200_OK)


class VerifyTokenView(GenericAPIView):
    """ Verify user token and send jwt token """
    serializer_class = VerifyTokenSerializer

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = serialized.get_user()
        response = generate_jwt_for_user(user)
        return Response(response, status=status.HTTP_200_OK)


class UpdateProfileView(GenericAPIView):
    """ Get and update profile object """

    def get(self, request, *args, **kwargs):
        """ return profile object """
        serialized = self.get_serializer(request.user.profile, context={"request": request})
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """ update existing profile object """
        serialized = self.get_serializer(request.user.profile, data=request.data, partial=True, context={"user": request.user})
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return ProfileCreationSerializer(*args, **kwargs)
        elif self.request.method == 'PUT':
            return ProfileUpdateSerializer(*args, **kwargs)
    