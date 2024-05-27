from django.urls import path
from base.general.views import WorkoutGifListView, ClientListView


urlpatterns = [
    path('gifs/', WorkoutGifListView.as_view(), name="listing_gits"),
    path('clients/', ClientListView.as_view(), name="clients_says"),  
]