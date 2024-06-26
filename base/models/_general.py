from django.db import models
from base.models import BaseModel


class ExerciseTypeChoices(models.TextChoices):
    """ choices about what is the meaning of each exercise type """
    PUSH_UP = 'push_up', "Push Up"
    PULL_UP = 'pull_up', "Pull UP"
    PLANK = 'plank', 'Plank'
    CRUNCH = 'crunch', 'Crunch'
    SQUAT = 'squat', 'Squat'


class ExerciseStatusChoices(models.TextChoices):
    """ choices for different status """
    CREATED = 'created', 'Created'
    DOING = 'doing', 'Doing'
    DONE = 'done', 'Done'


class Exercise(BaseModel):
    """ store each exercise which is done by user """
    # Textual data fields
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ExerciseTypeChoices.choices)
    token = models.UUIDField()
    status = models.CharField(max_length=10, choices=ExerciseStatusChoices.choices, default=ExerciseStatusChoices.CREATED.value)

    # Numerical data fields
    repeatation = models.PositiveSmallIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="exercise_images/")

    # Relational data fields
    profile = models.ForeignKey("base.Profile", on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return f"Exercise Object: {self.id} - {self.get_type_display()} - {self.repeatation}"


class WorkoutGif(BaseModel):
    """ Store each gif and its creation date """
    gif = models.FileField(upload_to='gifs/')

    def __str__(self):
        return f"WorkoutGif Object: {self.id}"


class Client(models.Model):
    """ What clients says """

    # Textual content
    name = models.CharField(max_length=100)
    opinion = models.TextField()

    # image content
    image = models.ImageField(upload_to='clients_avatar/')

    def __str__(self):
        return f"Client Objects: {self.id} - {self.name}"