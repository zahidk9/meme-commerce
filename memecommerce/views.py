from django.shortcuts import render
from memecommerce.models import Meme
from django.http import HttpResponse

# Create your views here.

def home(request):
    context_dict = {}
    response = render(request, 'memecommerce/home.html', context=context_dict)
    return response

def about(request):
    context_dict = {}
    response = render(request, 'memecommerce/about.html', context=context_dict)
    return response


# meme-related views
def viewMeme(request, meme_slug):
    context_dict = {}

    try:
        meme = Meme.objects.get(slug=meme_slug)
        context_dict[meme] = meme

    except Meme.DoesNotExist:
        context_dict[meme] = None

    return render(request, 'memecommerce/viewMeme.html', context=context_dict)

def buyMeme(request, meme_slug):
    context_dict = {}

    try:
        meme = Meme.objects.get(slug=meme_slug)
        context_dict[meme] = meme

    except Meme.DoesNotExist:
        context_dict[meme] = None

    return render(request, 'memecommerce/buyMeme.html', context=context_dict)

def sellMeme(request):
    context_dict = {}
    response = render(request, 'memecommerce/sellMeme.html', context=context_dict)
    return response


# account-related views
def account(request):
    context_dict = {}
    response = render(request, 'memecommerce/account.html', context=context_dict)
    return response

def editAccount(request):
    context_dict = {}
    response = render(request, 'memecommerce/editAccount.html', context=context_dict)
    return response

def myListings(request):
    context_dict = {}
    response = render(request, 'memecommerce/myListings.html', context=context_dict)
    return response

def myMemes(request):
    context_dict = {}
    response = render(request, 'memecommerce/myMemes.html', context=context_dict)
    return response

# authentication-related views
def login(request):
    context_dict = {}
    response = render(request, 'memecommerce/login.html', context=context_dict)
    return response

def register(request):
    context_dict = {}
    response = render(request, 'memecommerce/register.html', context=context_dict)
    return response