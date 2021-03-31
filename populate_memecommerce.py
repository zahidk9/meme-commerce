import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memecommerce_project.settings')

import django
django.setup()
from memecommerce.models import Meme, MemeBasket, MemeOrder, UserProfile

def populate():
    pass

if __name__ == '__main__':
    print('Starting Memecommerce population script...')
    populate()