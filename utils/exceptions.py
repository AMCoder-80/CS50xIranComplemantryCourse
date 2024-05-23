from rest_framework.exceptions import APIException
from rest_framework import status


class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'An error occured'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: detail}
        
        else: self.detail = {'detail': self.default_detail}
