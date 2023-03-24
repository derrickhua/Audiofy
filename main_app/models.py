from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# for models associated in 1:M relationship with the user, add this: 
# user = models.ForeignKey(User, on_delete=models.CASCADE)


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'test_id': self.id})
    
