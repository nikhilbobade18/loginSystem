from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User)

    client_name = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=50)
    email = models.TextField(max_length=30)

    def __str__(self):
        return self.client_name
