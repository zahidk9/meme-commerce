from django.urls import path
from memecommerce import views

app_name = 'memecommerce'

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('sellmeme', views.sellmeme, name='sellmeme'),
	path('account', views.account, name='account'),
	path('account/edit', views.editAccount, name='editAccount'),
	path('account/memes', views.myMemes, name='myMemes'),
	path('login', views.login, name='login'),
	path('register', views.register, name='register')
]
