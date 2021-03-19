from django.db import models
from django.conf import settings

#meme's split into three sections. Before purchase, in basket and 
#post order. Post order is where the users memes are stored
class Meme(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
class MemeBasket(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class MemeOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    memes = models.ManyToManyField(MemeBasket)
    meme_ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username