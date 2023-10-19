from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models


class ExtendedGroup(Group):
    description = models.TextField(blank=True, null=True)
