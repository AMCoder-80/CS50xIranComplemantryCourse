from django.urls import path
from base.views import home

urlpatterns = [
    path("", home, name="main_view")
]