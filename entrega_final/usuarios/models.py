from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InfoExtra(models.Model):
    avatar = models.ImageField(upload_to='media', null=True, blank=True)
    website = models.URLField(null=True, default="none")
    user = models.OneToOneField(User, on_delete=models.CASCADE)