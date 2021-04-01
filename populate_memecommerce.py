import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memecommerce_project.settings')

import django
django.setup()
from memecommerce.models import Meme, MemeOrder, MemeListing, UserProfile

def populate():
    memes = [
    {'title': 'Bernie stays drippin',
        'price': 10.00,
        'description': 'Bernie Sanders at the inauguration of Joe Biden.',
        'image': 'media/memes/bernie_at_inauguration.jpg'},    
    {'title': 'The Weeknd loses his mind',
        'price': 12.99,
        'description': 'The Weeknd performance at SuperBowl 55.',
        'image': 'media/memes/theweeknd_loses_mind.jpeg'},
    {'title': 'Distracted Boyfriend',
        'price': 3.99,
        'description': 'Boyfriend willing to risk it all.',
        'image': 'media/memes/distracted_boyfriend.jpg'},
    {'title': 'Blinking Guy',
        'price': 4.20,
        'description': 'This man blinks and we are eternally grateful.',
        'image': 'media/memes/blinking_guy.jpg'},
    {'title': 'MJ takes it personally',
        'price': 6.23,
        'description': 'He really do be taking it personally tho.',
        'image':'media/memes/mj_takes_it_personally.jpeg'}]

    for meme in memes:
        for k, v in meme.items():
            m = add_meme(title=meme['title'], price=meme['price'], description=meme['description'], image=meme['image'])
    for m in Meme.objects.all():
        print(f'- {m}')

def add_meme(title, price, description, image):
    m = Meme.objects.get_or_create(title=title)[0]
    m.price=price
    m.description=description
    m.image=image
    m.save()
    return m 

if __name__ == '__main__':
    print('Starting Memecommerce population script...')
    populate()