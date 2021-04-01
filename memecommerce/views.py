from django.shortcuts import render
from memecommerce.models import Meme
from django.http import HttpResponse
from memecommerce.forms import UserForm, UserProfileForm

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
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm() 
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'memecommerce/register.html', context=context_dict)