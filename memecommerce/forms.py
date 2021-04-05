from django import forms
from django.contrib.auth.models import User 
from memecommerce.models import Meme, UserProfile
from django.contrib.auth.forms import UserChangeForm

class MemeForm(forms.ModelForm):
    title = forms.CharField(max_length=32)
    price = forms.DecimalField(decimal_places=2, min_value=0, max_digits=6)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.TextInput(), required=False)

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

class EditAccountForm(UserChangeForm):
    template_name = 'memecommerce/editAccount.html'
    class Meta:
        model = User 
        fields = ('email',)

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = []