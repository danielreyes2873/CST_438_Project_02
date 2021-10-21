
from django.urls import path
from . import views

urlpatterns= [
    path('', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
]