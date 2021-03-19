from django.contrib import admin

# Register your models here.
from .models import Meme, MemeBasket, MemeOrder

admin.site.register(Meme)
admin.site.register(MemeBasket)
admin.site.register(MemeOrder)