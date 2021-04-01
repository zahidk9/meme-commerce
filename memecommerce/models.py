from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#meme's are split into them being either ordered or listed by the user
#with each of these splits inheriting from the main Meme class
class Meme(models.Model):
    title = models.CharField(max_length=100, db_index=True, unique=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = models.ImageField(upload_to= 'memes/', blank=True)
#slug allows users meme names to be converted to url's
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    purchased = models.BooleanField(default=False)
    listed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Meme, self).save(*args, **kwargs)
    
    def meme_purchase(self):
        purchased = True
        return

    def meme_listing(self):
        listed = True
        return

class MemeOrder(models.Model):
    ordered_meme = models.OneToOneField(Meme, null=True, on_delete=models.CASCADE)
    meme_ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.__class__)

class MemeListing(models.Model):
    listed_meme = models.OneToOneField(Meme, null=True, on_delete=models.CASCADE)
    meme_listed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.__class__)
        

class UserProfile(models.Model):
    #this links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_memes = models.ForeignKey(MemeOrder, null=True, blank=True, on_delete=models.CASCADE)
    listed_memes = models.ForeignKey(Meme, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
       return self.user.username


