from django.urls import path
from base.accounts.views import (
    UserCreationView, ProfileCreationView,
    LoginRequestView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # path('signup/', create_user, name="create_new_user"),   
    path('signup/', UserCreationView.as_view(), name="create_new_user"),
    path('signin/', LoginRequestView.as_view(), name="login_request"),
    path('profile/create/', ProfileCreationView.as_view(), name="create_new_profile"),
    # rest default routes
    path('login/', TokenObtainPairView.as_view(), name='login_with_password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]