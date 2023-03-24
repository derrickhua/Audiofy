from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Anything related to Test Model
    path('tests/', views.tests_index, name='index'),
    path('tests/<int:test_id>/', views.tests_detail, name='detail'),
    path('tests/create/', views.TestCreate.as_view(), name='tests_create'),
    path('tests/<int:pk>/update/', views.TestUpdate.as_view(), name='tests_update'),
    path('tests/<int:pk>/delete/', views.TestDelete.as_view(), name='tests_delete'),
    # Anything related to authentication
    path('accounts/signup/', views.signup, name='signup'),
    path('loggedin/', views.loggedin, name='loggedin'),
]
