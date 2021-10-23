from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<slug:id>', views.index2, name="index2"),
    path('deleteItem/<slug:id>', views.index3, name="index3")
]
