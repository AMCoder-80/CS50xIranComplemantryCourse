from django.urls import path, include


urlpatterns = [
    path('user/',include("base.accounts.urls")),
    path('general/',include("base.general.urls")),
]