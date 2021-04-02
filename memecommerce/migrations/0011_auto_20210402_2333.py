# Generated by Django 2.2.17 on 2021-04-02 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memecommerce', '0010_auto_20210401_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memeorder',
            name='ordered_meme',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='listed',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='purchased',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='listed_memes',
        ),
        migrations.AddField(
            model_name='meme',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meme',
            name='meme_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meme',
            name='description',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.ImageField(upload_to='memes/'),
        ),
        migrations.AlterField(
            model_name='meme',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='meme',
            name='title',
            field=models.CharField(max_length=32),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='purchased_memes',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='purchased_memes',
            field=models.ManyToManyField(to='memecommerce.Meme'),
        ),
        migrations.DeleteModel(
            name='MemeListing',
        ),
        migrations.DeleteModel(
            name='MemeOrder',
        ),
    ]
