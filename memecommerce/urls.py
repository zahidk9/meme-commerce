from django.urls import path
from memecommerce import views

app_name = 'memecommerce'

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('404/', views.missing, name='404'),

	path('viewmeme/<uuid:meme_id>/', views.viewMeme, name='viewMeme'),
	path('buymeme/<uuid:meme_id>/', views.buyMeme, name='buyMeme'),
	path('sellmeme/', views.sellMeme, name='sellMeme'),

	path('account/', views.account, name='account'),
	path('account/edit/', views.editAccount, name='editAccount'),
	path('account/delete/', views.deleteAccount, name='deleteAccount'),
	path('account/listings/', views.myListings, name='myListings'),
	path('account/memes/', views.myMemes, name='myMemes'),

	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.register, name='register')
]
