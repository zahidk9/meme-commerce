from django.contrib import admin
from memecommerce.models import Meme, MemeOrder, MemeListing, UserProfile

admin.site.register(Meme)
admin.site.register(MemeListing)
admin.site.register(MemeOrder)
admin.site.register(UserProfile)