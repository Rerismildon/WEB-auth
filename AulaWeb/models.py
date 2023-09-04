from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    