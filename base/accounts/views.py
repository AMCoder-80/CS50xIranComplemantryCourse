# django related modules

# DRF related modules
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView

# Local modules
from base.accounts.serializers import CreateUserSerializer
from base.models import User
# Third party modules


# @api_view(['POST'])
# def create_user(request):
#     """ Create new user """
#     if request.method == 'POST':
#         serialized = CreateUserSerializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.data, status=status.HTTP_200_OK)


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
