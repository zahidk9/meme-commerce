from django import forms
from memecommerce.models import Meme, MemeBasket, MemeOrder, UserProfile
#any help in this would be greatly appreciated as I honestly have no clue
#what I am doing

class MemeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the name of your meme.")
    description = forms.TextField(null=True, blank=True, help_text="Please enter a description of your meme (optional)")
    price = forms.FloatField(required=True, "Please enter a price for your meme")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Meme 
        fields = ('title', 'description', 'price')

class MemeBasketForm(forms.ModelForm):
    meme_ordered = forms.BooleanField(default=False)
#how to do this with a foriegn key?