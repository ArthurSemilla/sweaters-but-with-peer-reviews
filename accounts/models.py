from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#This Model can be used to store more data about the user
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, null=True)
    key_expires = models.DateTimeField(default=timezone.now())
      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'