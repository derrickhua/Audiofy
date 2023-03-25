from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# for models associated in 1:M relationship with the user, add this: 
# user = models.ForeignKey(User, on_delete=models.CASCADE)

class Song(models.Model):
    """
    Songs do not have CRUD functionality, you can only like a song, update a playlist with a song or delete a song from a playlist
    therefore the important related routes are associating or unassociating it with a playlist
    """
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=15)
    album = models.CharField(max_length=50)
    explicit = models.BooleanField()

    # same as playlist
    likes = models.IntegerField()

    # the value input into here will be found through the file in AWS
    duration = models.DurationField()

    # Unlike Playlist the Song's image will not be upladed and is instead inherent
    cover_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})
  

class Song(models.Model):
    """
    Artists do not have CRUD functionality, you can only like or follow an artist
    therefore the important related routes are associating or unassociating it with a playlist
    """
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=15)
    album = models.CharField(max_length=50)
    explicit = models.BooleanField()

    # same as playlist
    likes = models.IntegerField()

    # the value input into here will be found through the file in AWS
    duration = models.DurationField()

    # Unlike Playlist the Song's image will not be upladed and is instead inherent
    cover_url = models.URLField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})


class Playlist(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    # This duration will have to be calculated after returning each song's duration
    # we will be using the datetime library and specifically datetime.timedelta(hours=?, minutes=?, seconds=?)
    duration = models.DurationField()

    # You should be capable of uploading an image to the playlist else default / which will be stored in AWS
    # there are then 2 AWS buckets: songs, playlist images
    # the height and width of the img will be adjusted within a div + CSS 
    image_url = models.ImageField()

    # Automatically sets the field to now when the object is first created / basically a timestamp
    date_created = models.DateField(auto_now_add=True)

    # Need to make something that tracks likes / i.e. everytime button is pressed, the playlist gets another user attached to it
    # else it's just a number field using js to update +1 everytime the button is hit
    likes = models.IntegerField()

    # attach M:M relationship with songs
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'test_id': self.id})





