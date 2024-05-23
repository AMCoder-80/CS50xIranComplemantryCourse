from django.urls import path
from base.accounts.views import (
    UserCreationView, ProfileCreationView
)


urlpatterns = [
    # path('signup/', create_user, name="create_new_user"),   
    path('signup/', UserCreationView.as_view(), name="create_new_user"),
    path('profile/create/', ProfileCreationView.as_view(), name="create_new_profile"),   
]