from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
import helpers

def get_image_path(instance, filename):
    basename, format = os.path.splitext(filename)
    new_filename = instance.user.id + format
    return os.path.join('avatars', new_filename)

class Profile(models.Model):
    user                    = models.OneToOneField(User)
    twitter_username        = models.CharField(max_length=256)
    twitter_key             = models.CharField(max_length=256)
    avatar                  = ImageField(upload_to=get_image_path)
    job_title               = models.CharField(max_length=256)
