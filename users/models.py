from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    balance = models.PositiveSmallIntegerField(default=0)
    pass
