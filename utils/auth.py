from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login


def generate_jwt_for_user(user):
    """ Generate refresh and access token for each user """
    token = RefreshToken.for_user(user)
    update_last_login(None, user)

    response = {
        "refresh": str(token),
        "access": str(token.access_token)
    }
    return response
