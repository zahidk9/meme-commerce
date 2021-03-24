from django.contrib import admin
from memecommerce.models import UserProfile
# Register your models here.
from .models import Meme, MemeBasket, MemeOrder

admin.site.register(Meme)
admin.site.register(MemeBasket)
admin.site.register(MemeOrder)
admin.site.register(UserProfile)