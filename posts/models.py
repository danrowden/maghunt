from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

import countries

def get_image_path(instance, filename):
    basename, format = os.path.splitext(filename)
    new_filename = instance.id + format
    return os.path.join('covers', new_filename)

class Post(models.Model):
    date_submitted      = models.DateTimeField(auto_now_add=True)
    date_posted         = models.DateTimeField(null=True)
    submitter           = models.ForeignKey(User)
    poster              = models.ForeignKey(User, null=True, related_name='poster')
    magazine            = models.CharField(max_length=50)
    magpile_magazine_id = models.PositiveIntegerField(null=True)
    issue               = models.CharField(max_length=50)
    magpile_issue_id    = models.PositiveIntegerField(null=True)
    slug                = models.SlugField()
    cover               = ImageField(upload_to=get_image_path)
    genre               = models.CharField(max_length=40)
    country             = countries.CountryField()
    url                 = models.URLField()
    price               = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    price_currency      = models.CharField(max_length=4)
    buy_url             = models.URLField()

class Vote(models.Model):
    UP_VOTE_TYPE = 'u'
    DOWN_VOTE_TYPE = 'd'
    VOTE_CHOICES = (
        (UP_VOTE_TYPE, 'Upvote'),
        (DOWN_VOTE_TYPE, 'Downvote'),
    )
    type        = models.CharField(choices=VOTE_CHOICES, max_length=1)
    date        = models.DateTimeField(auto_now_add=True)
    post        = models.ForeignKey(Post)
    user        = models.ForeignKey(User)

class Comment(models.Model):
    date            = models.DateTimeField(auto_now_add=True)
    post            = models.ForeignKey(Post)
    user            = models.ForeignKey(User)
    text            = models.TextField()
    text_markdown   = models.TextField()

    # save markdown version, with formatting, URLs and user @ links
