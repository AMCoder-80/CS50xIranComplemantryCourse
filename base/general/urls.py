from django.urls import path
from base.general.views import WorkoutGifListView


urlpatterns = [
    path('gifs/', WorkoutGifListView.as_view(), name="listing_gits")    
]