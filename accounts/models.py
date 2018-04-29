from django.db import models
from django.contrib.auth.models import User
import os


def upload_full_image(instance, filename):
    return "avatars/%s%s%s" % (instance.id, hashing(), os.path.splitext(filename)[1])


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])