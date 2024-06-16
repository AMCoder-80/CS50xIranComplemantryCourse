# Django related modules
from django.shortcuts import get_object_or_404

# DRF modules
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView

# Local modules
from base.models import WorkoutGif, Client, Exercise
from base.general.serializers import (
    WorkoutGifListSerializer, ClientListSerializer,
    ExerciseListSerializer, CreateExerciseSerializer,
    ExerciseUpdateSerializer
    )


class WorkoutGifListView(ListAPIView):
    """ Listing all gifts """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()


class ClientListView(ListAPIView):
    """ Listing all clients """
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class ExerciseListView(ListCreateAPIView):
    """ Listing all exercises and create new ones"""
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return CreateExerciseSerializer
        elif self.request.method == 'GET':
            return ExerciseListSerializer

    def get_queryset(self):
        return Exercise.objects.filter(profile=self.request.user.profile)


class GetExerciseView(RetrieveUpdateAPIView):
    """ Return a single exercise object """
    serializer_class = ExerciseUpdateSerializer
    queryset = Exercise.objects.all()
    lookup_field = 'token'
