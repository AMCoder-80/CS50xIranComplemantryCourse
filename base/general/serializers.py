from rest_framework import serializers
from base.models import WorkoutGif, Client, Exercise
import uuid


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
    status = serializers.SerializerMethodField(method_name="get_status")
    class Meta:
        model = Exercise
        fields = ('id', 'title', 'repeatation', 'token', 'status', 'duration', 'type', 'image')

    def get_type(self, obj: Exercise):
        return obj.get_type_display()
    
    def get_status(self, obj: Exercise):
        return obj.get_status_display()
    

class CreateExerciseSerializer(serializers.ModelSerializer):
    """ create a new object with some fields """
    class Meta:
        model = Exercise
        fields = ("title", "type", "token")
        read_only_fields = ("token", )

    def create(self, validated_data):
        # generate a unique identifier value
        unique_value = str(uuid.uuid4())
        request = self.context['request']
        exercise = Exercise.objects.create(
            token=unique_value,
            profile=request.user.profile,
            image=f"exercise_images/{validated_data['type']}.jpeg",
            **validated_data
        )
        return exercise
