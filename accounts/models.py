from django.contrib.auth.models import User as UserBase
from django.db import models


class User(UserBase):
    """Customization to adding useful methods."""

    class Meta:
        proxy = True
        ordering = ('first_name', 'last_name', )


class Profile(models.Model):
    """To store additional data for user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
