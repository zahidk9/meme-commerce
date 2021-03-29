from django.urls import path
from memecommerce import views

app_name = 'memecommerce'

urlpatterns = [
	path('cow', views.cow, name='cow')
]
