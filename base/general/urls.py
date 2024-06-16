from django.urls import path
from base.general.views import (
    WorkoutGifListView, ClientListView,
    ExerciseListView, GetExerciseView
    )


urlpatterns = [
    path('gifs/', WorkoutGifListView.as_view(), name="listing_gits"),
    path('clients/', ClientListView.as_view(), name="clients_says"),  
    path('workout/', ExerciseListView.as_view(), name="list_workouts"),
    path('workout/<str:token>/', GetExerciseView.as_view(), name="get_single_workout"),
]