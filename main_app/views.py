# All modules necessary for Django to work
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# All modules necessary for Photo Uploading and AWS storage uploading
import uuid
import boto3

from .models import Playlist

# We will need this once we need to add more forms
# from .forms import SomeForm

# Things we will need once we set up AWS
# S3_BASE_URL = 's3.ca-central-1.amazonaws.com/'
# BUCKET = 'needtosetup'



def landing_page(request):
  return render(request, 'landing_page.html')

@login_required
def playlist_index(request):
  return render(request, 'index.html')


class PlaylistCreate(LoginRequiredMixin, CreateView):
  model = Playlist
  fields = ['name']
  # This will assign a future TestModel to the currently logged in user
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
  model = Playlist
  fields = ['name']

class PlaylistDelete(LoginRequiredMixin, DeleteView):
  model = Playlist
  success_url = '/playlists'

@login_required
def playlist_detail(request, test_id):
  playlists = Playlist.objects.get(id=test_id)
  return render(request, 'playlist/detail.html', {
    'playlists': playlists, 
  })

@login_required
def playlist_index(request):
  playlists = Playlist.objects.filter(user=request.user)
  return render(request, 'playlist/index.html', { 'playlist': playlists })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
