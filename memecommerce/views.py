from django.shortcuts import render
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

def sellMeme(request):
    context_dict = {}
    response = render(request, 'memecommerce/sellMeme.html', context=context_dict)
    return response

def account(request):
    context_dict = {}
    response = render(request, 'memecommerce/account.html', context=context_dict)
    return response

def editAccount(request):
    context_dict = {}
    response = render(request, 'memecommerce/editAccount.html', context=context_dict)
    return response

def myMemes(request):
    context_dict = {}
    response = render(request, 'memecommerce/myMemes.html', context=context_dict)
    return response

def login(request):
    context_dict = {}
    response = render(request, 'memecommerce/login.html', context=context_dict)
    return response

def register(request):
    context_dict = {}
    response = render(request, 'memecommerce/register.html', context=context_dict)
    return response