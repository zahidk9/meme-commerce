from django.contrib import admin
from memecommerce.models import Meme, MemeOrder, UserProfile

admin.site.register(Meme)
#admin.site.register(MemeBasket)
admin.site.register(MemeOrder)
admin.site.register(UserProfile)