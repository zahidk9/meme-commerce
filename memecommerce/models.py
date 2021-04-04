import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Meme(models.Model):
    # primary key. generates a unique key so that memes may have duplicate names
    meme_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # if an author deletes their account, all of their memes will be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # blank and null temporarily until user accounts work properly
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to="memes/")
    description = models.TextField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Meme, self).save(*args, **kwargs)
        

class UserProfile(models.Model):
    # this links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_memes = models.ManyToManyField(Meme, blank=True)
    # no args function can be called like {{ user.listed_memes }} in template
    def listed_memes(self):
        return self.user.meme_set.all()

    def __str__(self):
       return self.user.username


