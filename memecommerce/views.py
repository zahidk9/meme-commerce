from django.shortcuts import render


# Create your views here.

# Just a temporary view function for the homepage
def cow(request):
    print("cow")
    return render(request, 'memecommerce/cow.html')
