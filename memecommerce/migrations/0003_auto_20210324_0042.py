# Generated by Django 2.2.17 on 2021-03-24 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memecommerce', '0002_auto_20210323_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memebasket',
            name='user',
        ),
        migrations.RemoveField(
            model_name='memeorder',
            name='user',
        ),
    ]
