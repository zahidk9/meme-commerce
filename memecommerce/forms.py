from django import forms
from django.contrib.auth.models import User 
from memecommerce.models import Meme, MemeOrder, UserProfile

class MemeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, db_index=True, help_text="Please enter the name of your meme.")
    price = forms.DecimalField(required=True, "Please enter a price for your meme")
    image = forms.ImageField(upload_to= 'memes/', blank=True, help_text="Upload your image here.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.TextField(null=True, blank=True, help_text="Please enter a description of your meme (optional)")
    
    class Meta:
        model = Meme 
        fields = ('title', 'description', 'price')


class MemeOrderForm(forms.ModelForm):
    class Meta:
        model = MemeOrder 
        fields = ('Ordered Meme')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('purchased', 'listed',)