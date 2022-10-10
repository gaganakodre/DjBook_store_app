from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from .jwt_service import JwtService


class User(AbstractUser):
    phone_number = models.BigIntegerField(default=0)
    location = models.CharField(max_length=255,default="blank")
    is_verified = models.BooleanField(default=False)

    @property
    def token(self):
        """
        this token property is used while login after verification
        """
        return JwtService().encode({"user_id": self.id, "username": self.username})