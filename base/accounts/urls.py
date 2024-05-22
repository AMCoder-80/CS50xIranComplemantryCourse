from django.urls import path
from base.accounts.views import CreateUserView


urlpatterns = [
    # path('signup/', create_user, name="create_new_user"),   
    path('signup/', CreateUserView.as_view(), name="create_new_user"),   
]