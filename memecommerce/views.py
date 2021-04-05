from uuid import UUID

import time
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import View, TemplateView 
from memecommerce.models import Meme, UserProfile
from django.http import HttpResponse, JsonResponse
from memecommerce.forms import UserForm, UserProfileForm, MemeForm, EditAccountForm, UserDeleteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#class MainView(TemplateView):
    #template_name = 'memecommerce/home.html'

#class PostJsonListView(View):
    #def get(self, *args, **kwargs):
        #print(kwargs)
        #upper = kwargs.get('num_posts')
        #lower = upper - 6
        #posts = list(Meme.objects.values()[lower:upper])
        #posts_size = len(Meme.objects.all())
        #max_size = True if upper >= posts_size else False
        #return JsonResponse({'data': posts, 'max': max_size}, safe=False)

def home(request):
    meme_list = list(filter(lambda meme: meme.purchased == False, Meme.objects.order_by('-created')))[0:]

    context_dict = {}
    context_dict['meme_list'] = meme_list

    response = render(request, 'memecommerce/home.html', context=context_dict)
    return response

def about(request):
    context_dict = {}
    response = render(request, 'memecommerce/about.html', context=context_dict)
    return response

def missing(request):
    return render(request, 'memecommerce/404.html')


# meme-related views
def viewMeme(request, meme_id):
    context_dict = {}

    try:
        meme = Meme.objects.get(meme_id=meme_id)
        context_dict['meme'] = meme

    except Meme.DoesNotExist:
        context_dict['meme'] = None
        return redirect(reverse('memecommerce:404'))

    print("context_dict:" + str(context_dict))

    return render(request, 'memecommerce/viewMeme.html', context=context_dict)

@login_required
def buyMeme(request, meme_id):
    context_dict = {}
    try:
        meme = Meme.objects.get(meme_id=meme_id)
        context_dict[meme] = meme

        if request.method == 'POST':
            user = request.user
            userprofile = UserProfile.objects.get(user=user)
            userprofile.purchased_memes.add()
            redirect(reverse('memecommerce:home'))

    except Meme.DoesNotExist:
        context_dict[meme] = None
        return redirect(reverse('memecommerce:404'))

    return render(request, 'memecommerce/buyMeme.html', context=context_dict)

@login_required
def sellMeme(request):
    if request.method == 'POST':
        meme_form = MemeForm(request.POST, request.FILES)

        if meme_form.is_valid():
            meme = meme_form.save()
            meme.author = request.user
            meme.created = int(time.time())
            meme.save()
            return redirect(reverse('memecommerce:home'))
        else:
            print(meme_form.errors)
    else:
        meme_form = MemeForm()
    context_dict = {'meme_form': meme_form}
    return render(request, 'memecommerce/sellMeme.html', context=context_dict)


# account-related views
@login_required
def account(request):
    myaccount = UserProfile.objects.all()
    
    context_dict = {}
    context_dict['myaccount'] = myaccount
    
    response = render(request, 'memecommerce/account.html', context=context_dict)
    return response
@login_required
def editAccount(request):
    if request.method == 'POST':
        forms = EditAccountForm(request.POST, instance=request.user)

        if forms.is_valid():
            forms.save()
            return redirect(reverse('memecommerce:account'))
    else:
        form = EditAccountForm(instance=request.user)
        args = {'form': form}
        return render(request, 'memecommerce/editAccount.html', args)

@login_required
def deleteAccount(request):
    if request.method == "POST":
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user 
        user.delete()
        messages.info(request, 'Your account has been deleted')
        return redirect(reverse('memecommerce:home'))
    else:
        delete_form = UserDeleteForm(instance=request.user)
    
    context = {
        'delete_form': delete_form
    }

    return render(request, "memecommerce/deleteAccount.html", context)

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
            return redirect(reverse('memecommerce:login'))
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