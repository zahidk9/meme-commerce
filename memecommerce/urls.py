from django.urls import path
from memecommerce import views

app_name = 'memecommerce'

urlpatterns = [
	path('', views.cow, name='cow')
]
