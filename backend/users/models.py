from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class HGFJHf(models.Model):
    "Generated Model"
    hgffhgfhg = models.BigIntegerField()


class JHGHFjg(models.Model):
    "Generated Model"
    fghfgjety = models.BigIntegerField()


class GHjhg(models.Model):
    "Generated Model"
    fgsfhs = models.BigIntegerField()
