# Generated by Django 4.1.7 on 2023-03-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_playlist_duration_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='image_url',
            field=models.CharField(max_length=200),
        ),
    ]
