import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memecommerce_project.settings')

import django
django.setup()
from memecommerce.models import Meme, UserProfile
def populate():
    memes = [
        {
            'title': 'surprised pikachu',
            'price': 27.00,
            'description': 'someone stole his ketchup',
            'image': 'media/memes/pikachu.png',
            'purchased': True,
        },
        {
            'title': 'good boy',
            'price': 1000,
            'description': 'a good boy indeed',
            'image': 'media/memes/snake.jpg',
            'purchased': False,
        },
        {
            'title': 'duck',
            'price': 8080,
            'description': 'what do u think',
            'image': 'media/memes/duck.PNG',
            'purchased': False,
        },
        {
            'title': 'super mario',
            'price': 64.00,
            'description': 'There is nothing wrong with him.',
            'image': 'media/memes/mario.png',
            'purchased': False,
        },
        {
            'title': 'baby bottle',
            'price': 4.20,
            'description': 'will relax the baby',
            'image': 'media/memes/bottle.png',
            'purchased': False,
        },
        {
            'title': 'cat jug',
            'price': 129.88,
            'description': 'your cat jug sir',
            'image': 'media/memes/cat_jug.jpg',
            'purchased': False,
        },
        {
            'title': 'monke on bus',
            'price': 3900,
            'description': 'monke will surpass us',
            'image': 'media/memes/cat.jpg',
            'purchased': False,
        },
        {
            'title': 'doge',
            'price': 0.01,
            'description': 'such classic',
            'image': 'media/memes/doge.jpg',
            'purchased': False,
        },
        {
            'title': 'fish',
            'price': 100.00,
            'description': 'he\'s looking at you.',
            'image': 'media/memes/fish.png',
            'purchased': False,
        },
        {
            'title': 'balloon',
            'price': 3.60,
            'description': 'ayy lmao',
            'image': 'media/memes/fL2bn-fa_400x400.jpg',
            'purchased': False,
        },
        {
            'title': 'goomba',
            'price': 12.80,
            'description': 'are you',
            'image': 'media/memes/goomba.png',
            'purchased': False,
        },
        {
            'title': 'seal',
            'price': 5000,
            'description': 'relaxing and enjoying himself',
            'image': 'media/memes/seal.png',
            'purchased': False,
        },
        {
            'title': 'when the imposter is sus',
            'price': 9999.99,
            'description': 'jerma985',
            'image': 'media/memes/sus.png',
            'purchased': False,
        },
        {
            'title': 'Bernie stays drippin',
            'price': 10.00,
            'description': 'Bernie Sanders at the inauguration of Joe Biden.',
            'image': 'media/memes/bernie_at_inauguration.jpg',
            'purchased': False,
        },
        {
            'title': 'The Weeknd loses his mind',
            'price': 12.99,
            'description': 'The Weeknd performance at SuperBowl 55.',
            'image': 'media/memes/theweeknd_loses_mind.jpeg',
            'purchased': False,
        },
        {
            'title': 'Distracted Boyfriend',
            'price': 3.99,
            'description': 'Boyfriend willing to risk it all.',
            'image': 'media/memes/distracted_boyfriend.jpg',
            'purchased': False,
        },
        {
            'title': 'Blinking Guy',
            'price': 4.20,
            'description': 'This man blinks and we are eternally grateful.',
            'image': 'media/memes/blinking_guy.jpg',
            'purchased': False,
        },
        {
            'title': 'MJ takes it personally',
            'price': 6.23,
            'description': 'He really do be taking it personally tho.',
            'image': 'media/memes/mj_takes_it_personally.jpeg',
            'purchased': False,
        }
    ]

    for meme in memes:
        add_meme(title=meme['title'], price=meme['price'], description=meme['description'], image=meme['image'])
    for m in Meme.objects.all():
        print(f'- {m}')

def add_meme(title, price, image, description):
    # uuid gets created automatically
    # author temporarily not required
    m = Meme()
    m.title = title
    m.price = price
    m.image = image
    m.description = description
    m.save()
    return m

if __name__ == '__main__':
    print('Starting Meme-Commerce population script...')
    populate()