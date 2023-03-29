from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    # Anything related to authentication
    path('accounts/signup/', views.signup, name='signup'),
    # Anything related to Test Model
    path('playlists/', views.playlist_index, name='index'),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlist_update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist_delete'),
    # Anything Related to Songs
    # Liking a Song
    path('song/like_song', views.like_song, name='like_song'),
    path('songs/', views.songs_index, name='songs_index'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    # Associate a Song with a Playlist
    path('playlists/<int:playlist_id>/assoc_song/<int:song_id>/', views.assoc_song, name='assoc_song'),
    # Unassociate a Song with a Playlist
    path('playlists/<int:playlist_id>/unassoc_song/<int:song_id>/', views.unassoc_song, name='unassoc_song'),
]
