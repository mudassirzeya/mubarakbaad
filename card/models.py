from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.


class Create_card(models.Model):
    # user = models.OneToOneField(
    #     User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True)
    random_str = models.CharField(max_length=200, null=True, blank=True)
    languages = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
            return str(self.id)
