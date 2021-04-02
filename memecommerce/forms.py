from django import forms
from django.contrib.auth.models import User 
from memecommerce.models import Meme, UserProfile

class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme 
        fields = ('title', 'price', 'image', 'description')

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=24)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    purchased_memes = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        fields = ('purchased_memes',)