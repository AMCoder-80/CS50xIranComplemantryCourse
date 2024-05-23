from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.encoding import force_str


class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'An error occured'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_str(detail)}
        
        else: self.detail = {'detail': force_str(self.default_detail)}
