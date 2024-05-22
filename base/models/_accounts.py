# Django related modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Local modules
from base.models import BaseModel


class UserManager(BaseUserManager):
    """ Custom user manager """

    def create_user(self, email, *extra_fields):
        """ Create normal users """
        extra_fields.setdetaul("is_active", True)
        if not extra_fields.get("is_active"):
            raise ValueError("is_active value is not valid")
        try:
            user = self.model(email=email, *extra_fields)
            user.save()
            return user
        except Exception as e:
            raise ValueError(e)
    
    def create_superuser(self, email, *extra_fields):
        """ Create super users """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_active"):
            raise ValueError("is_active value is not valid")
        if not extra_fields.get("is_staff"):
            raise ValueError("is_staff value is not valid")
        if not extra_fields.get("is_superuser"):
            raise ValueError("is_superuser value is not valid")
        return self.create_user(email, *extra_fields)


class User(AbstractBaseUser):
    """ Main model for storing user information """
    # personal data fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    # django related fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # date time related fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    objects = UserManager()
    
    def __str__(self):
        return f"User Object: {self.id} - {self.first_name} {self.last_name}"
