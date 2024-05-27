from rest_framework import serializers
from base.models import WorkoutGif


class WorkoutGifListSerializer(serializers.ModelSerializer):
    """ Workout gifs serializer """
    class Meta:
        model = WorkoutGif
        fields = ( 'id', 'gif' )
