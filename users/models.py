from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Additional fields can be added here if needed
    email = models.EmailField(unique=True)
