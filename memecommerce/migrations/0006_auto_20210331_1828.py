# Generated by Django 2.2.17 on 2021-03-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memecommerce', '0005_auto_20210331_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
