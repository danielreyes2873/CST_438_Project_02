
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('viewItem/<slug:name>', views.viewItem, name='viewItem')
]