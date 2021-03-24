from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#meme's split into three sections. Before purchase, in basket and 
#post order. Post order is where the users memes are stored
class Meme(models.Model):
    title = models.CharField(max_length=100) 
    price = models.FloatField()
#slug allows users meme names to be converted to url's
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Meme, self).save(*args, **kwargs)
    
class MemeBasket(models.Model):
    
    meme_ordered = models.BooleanField(default=False)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    #quantity gives ability to keep track of number of memes user adds to basket
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title

    def get_total_price(self):
        return self.quantity * self.price 

class MemeOrder(models.Model):
    
    memes = models.ManyToManyField(MemeBasket)
    meme_ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    #this links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    memes = models.ForeignKey(MemeOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#164
