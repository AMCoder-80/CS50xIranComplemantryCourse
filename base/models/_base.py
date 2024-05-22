from django.db import models


class BaseModel(models.Model):
    """ This is base model to store all shared fields """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
