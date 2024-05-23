from django.core.cache import cache
from utils.constants import Constants
from random import randint


class CachingProcedureHandler:
    """ Deal with setting and getting data from cache """
    def __init__(self) -> None:
        self.expiration = Constants.REDIS_EXPIRATION
        self.token_from = 1_000
        self.token_to = 9_999
        self.keys = {
            Constants.LOGIN_CACHE_TYPE: "USER_LOGIN",
            Constants.FORGET_PASS_CACHE_TYPE: "FORGET_PASSWORD",
        }

    def set_key(self, type, email, token):
        """ store a key in cache """
        key = self.keys[type]
        return cache.set(f"{email}:{key}", token, self.expiration)
    
    def get_key(self, type, email):
        """ get a value from cache """
        key = self.keys[type]
        return cache.get(f"{email}:{key}")
    
    def generate_token(self):
        """ generate a token for authentication """
        token = randint(self.token_from, self.token_to)
        return str(token)
