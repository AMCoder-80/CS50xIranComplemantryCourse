from rest_framework import serializers
from base.models import WorkoutGif, Client


class WorkoutGifListSerializer(serializers.ModelSerializer):
    """ Workout gifs serializer """
    class Meta:
        model = WorkoutGif
        fields = ( 'id', 'gif' )


class ClientListSerializer(serializers.ModelSerializer):
    """ What clients say serializer """
    class Meta:
        model = Client
        fields = ('id', 'name', 'opinion', 'image')
