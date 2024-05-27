from rest_framework import serializers
from base.models import WorkoutGif, Client, Exercise


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


class ExerciseListSerializer(serializers.ModelSerializer):
    """ List all exercise's data """
    type = serializers.SerializerMethodField(method_name="get_type")
    class Meta:
        model = Exercise
        fields = ('id', 'title', 'repeatation', 'duration', 'type', 'image')

    def get_type(self, obj: Exercise):
        return obj.get_type_display()
