from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# for models associated in 1:M relationship with the user, add this: 
# user = models.ForeignKey(User, on_delete=models.CASCADE)

# arn:aws:s3:::adiofyapp/*

class Song(models.Model):
    """
    Songs do not have CRUD functionality, you can only like a song, update a playlist with a song or delete a song from a playlist
    therefore the important related routes are associating or unassociating it with a playlist
    """
    title = models.CharField(max_length=40)
    # Possibly temporrary depending on if artist model will get used
    createdby = models.CharField(max_length=40)
    genre = models.CharField(max_length=15)
    album = models.CharField(max_length=50)
    explicit = models.BooleanField()

    # same as playlist
    likes = models.IntegerField(default=0)

    # the value input into here will be found through the file in AWS
    # change this into a number second to minutes 
    # duration = models.DurationField(default=timedelta(days =0, seconds = 68400))

    # Unlike Playlist the Song's image will not be upladed and is instead inherent
    cover_url = models.URLField()

    song_link = models.URLField(default='')

    liked_by = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})
  

class Artist(models.Model):
    """
    Artists do not have CRUD functionality, you can only like or follow an artist, and they have an M:M relation with songs
    therefore the important related routes are associating or unassociating it with songs
    """
    name = models.CharField(max_length=40)
    songs = models.ManyToManyField(Song)
    album = models.CharField(max_length=50)

    # same as playlist
    follows = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})


class Playlist(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    # This duration will have to be calculated after returning each song's duration
    # we will be goign through each song and adding duration of each to a sum then inputting into the playlist 

    # You should be capable of uploading an image to the playlist else default / which will be stored in AWS
    # there are then 2 AWS buckets: songs, playlist images
    # the height and width of the img will be adjusted within a div + CSS 
    image_url = models.URLField()

    # Automatically sets the field to when the object is first created / basically a timestamp
    date_created = models.DateField(auto_now_add=True)

    # Need to make something that tracks likes / i.e. everytime button is pressed, the playlist gets another user attached to it
    # else it's just a number field using js to update +1 everytime the button is hit
    likes = models.IntegerField(default=0)

    # attach M:M relationship with songs
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('playlist_detail', kwargs={'playlist_id': self.id})



