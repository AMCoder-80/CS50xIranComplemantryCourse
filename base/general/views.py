# DRF modules
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# Local modules
from base.models import WorkoutGif, Client, Exercise
from base.general.serializers import (
    WorkoutGifListSerializer, ClientListSerializer,
    ExerciseListSerializer
    )


class WorkoutGifListView(ListAPIView):
    """ Listing all gifts """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()


class ClientListView(ListAPIView):
    """ Listing all clients """
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class ExerciseListView(ListAPIView):
    """ Listing all exercises """
    serializer_class = ExerciseListSerializer
    
    def get_queryset(self):
        return Exercise.objects.filter(profile=self.request.user.profile)
