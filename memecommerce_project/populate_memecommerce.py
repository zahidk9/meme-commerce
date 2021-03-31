import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memecommerce_project.settings')

import django
django.setup()
from memecommerce.models import Meme, MemeBasket, MemeOrder, UserProfile

def populate():
    memes = [
    {'title': 'Bernie stays drippin',
        'price': 10.00,
        'description': 'Bernie Sanders at the inauguration of Joe Biden.'},
    {'title': 'The Weeknd loses his mind',
        'price': 12.99,
        'description': 'The Weeknd performance at SuperBowl 55.'},
    {'title': 'Distracted Boyfriend',
        'price': 3.99,
        'description': 'Boyfriend willing to risk it all.'},
    {'title': 'Blinking Guy',
        'price': 4.20,
        'description': 'This man blinks and we are eternally grateful.'},
    {'title': 'MJ takes it personally',
        'price': 6.23,
        'description': 'He really do be taking it personally tho.'}]

    for meme, meme_data in memes.items():
        m = add_meme(title=meme_data['title'], price=meme_data['price'], description=meme_data['description'])
    for m in Meme.objects.all():
        print(f'- {m}')

def add_meme(title, price, description):
    m = Meme.objects.get_or_create(title=title)[0]
    m.price=price
    m.description=description
    m.save()
    return m 

if __name__ == '__main__':
    print('Starting Memecommerce population script...')
    populate()