from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    name = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
