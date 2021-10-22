
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('viewItem/<int:id>', views.viewItem, name='viewItem'),
    path('wishList/<int:id>', views.wishList, name='wishList'),
]