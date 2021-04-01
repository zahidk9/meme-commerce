from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from memecommerce.models import Meme
from django.http import HttpResponse
from memecommerce.forms import UserForm, UserProfileForm
from django.urls import reverse

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
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('memecommerce:home'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Meme-Commerce account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
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