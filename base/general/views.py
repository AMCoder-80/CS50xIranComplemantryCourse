# DRF modules
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# Local modules
from base.models import WorkoutGif, Client
from base.general.serializers import WorkoutGifListSerializer, ClientListSerializer


class WorkoutGifListView(ListAPIView):
    """ Listing all gifts """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()


class ClientListView(ListAPIView):
    """ Listing all clients """
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()