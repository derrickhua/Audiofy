from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    # Anything related to Test Model
    path('playlists/', views.playlist_index, name='index'),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlist_update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist_delete'),
    # Anything related to authentication
    path('accounts/signup/', views.signup, name='signup'),
]
