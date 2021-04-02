from django import forms
from django.contrib.auth.models import User 
from memecommerce.models import Meme, MemeOrder, MemeListing, UserProfile

class MemeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the name of your meme.")
    price = forms.DecimalField(required=True, help_text="Please enter a price for your meme.")
    image = forms.ImageField(required=True, help_text="Upload your image here.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(required=False, help_text="Please enter a description of your meme (optional)")
    
    class Meta:
        model = Meme 
        fields = ('title', 'description', 'price',)


class MemeOrderForm(forms.ModelForm):
    class Meta:
        model = MemeOrder 
        fields = ('ordered_meme',)

class MemeListingForm(forms.ModelForm):
    class Meta:
        model = MemeListing
        fields = ('listed_meme',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    purchased_memes = forms.CharField(widget=forms.HiddenInput())
    listed_memes = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('purchased_memes', 'listed_memes',)