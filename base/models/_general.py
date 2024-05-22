from django.db import models
from base.models import BaseModel


class ExerciseTypeChoices(models.TextChoices):
    """ choices about what is the meaning of each exercise type """
    PUSH_UP = 'push_up', "Push Up"
    PULL_UP = 'pull_up', "Pull UP"
    PLANK = 'plank', 'Plank'
    CRUNCH = 'crunch', 'Crunch'
    SQUAT = 'squat', 'Squat'


class Exercise(BaseModel):
    """ store each exercise which is done by user """
    # Textual data fields
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ExerciseTypeChoices.choices)

    # Numerical data fields
    repeatation = models.PositiveSmallIntegerField()
    duration = models.PositiveIntegerField()

    # Relational data fields
    profile = models.ForeignKey("base.Profile", on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return f"Exercise Object: {self.id} - {self.get_type_display()} - {self.repeatation}"