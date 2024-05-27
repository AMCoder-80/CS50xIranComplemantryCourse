# DRF modules
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# Local modules
from base.models import WorkoutGif
from base.general.serializers import WorkoutGifListSerializer


class WorkoutGifListView(ListAPIView):
    """ Listing all gifts """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()
