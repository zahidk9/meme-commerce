# Generated by Django 2.2.17 on 2021-04-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memecommerce', '0015_auto_20210404_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='created',
            field=models.DecimalField(decimal_places=7, max_digits=16, null=True),
        ),
    ]
