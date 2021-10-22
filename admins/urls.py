
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('viewUsers', views.index2, name="index2"),
    path('createUserInfo', views.index3, name="index3"),
    path('updaterUserInfo', views.index5, name="index5"),
    path('updatingUsers', views.index6, name="index6"),
]