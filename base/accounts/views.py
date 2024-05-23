# django related modules

# DRF related modules
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView

# Local modules
from base.accounts.serializers import (
    UserCreationSerializer, ProfileCreationSerializer
)
from base.models import User, Profile
from utils.auth import generate_jwt_for_user

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
