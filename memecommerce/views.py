from django.shortcuts import render, redirect
from django.urls import reverse 
from memecommerce.models import Meme
from django.http import HttpResponse
from memecommerce.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

@login_required
def buyMeme(request, meme_slug):
    context_dict = {}

    try:
        meme = Meme.objects.get(slug=meme_slug)
        context_dict[meme] = meme

    except Meme.DoesNotExist:
        context_dict[meme] = None

    return render(request, 'memecommerce/buyMeme.html', context=context_dict)

@login_required
def sellMeme(request):
    context_dict = {}
    response = render(request, 'memecommerce/sellMeme.html', context=context_dict)
    return response


# account-related views
@login_required
def account(request):
    context_dict = {}
    response = render(request, 'memecommerce/account.html', context=context_dict)
    return response
@login_required
def editAccount(request):
    context_dict = {}
    response = render(request, 'memecommerce/editAccount.html', context=context_dict)
    return response
@login_required
def myListings(request):
    context_dict = {}
    response = render(request, 'memecommerce/myListings.html', context=context_dict)
    return response
@login_required
def myMemes(request):
    context_dict = {}
    response = render(request, 'memecommerce/myMemes.html', context=context_dict)
    return response

# authentication-related views
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('memecommerce:home'))
            else:
                return HttpResponse("Your memecommerce account has been disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'memecommerce/login.html')

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

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('memecommerce:home'))