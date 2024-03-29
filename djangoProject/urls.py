"""djangoProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from database import views
from django.conf.urls import include
from register import views as v
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('admins.urls')),
    path('admins/viewUsers', include('admins.urls')),
    path('admins/createUserInfo', include('admins.urls')),
    path('admins/updaterUserInfo', include('admins.urls')),
    path('admins/updatingUsers', include('admins.urls')),
    # path('createUserInfo/', include('admins.urls')),
    # path("<int:userID>", views.index, name="index"),
    path('register/', v.register, name="register"),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('list/', include('list.urls')),
    path('list/viewItem/<int:id>', include('list.urls')),
    path('list/wishList/<int:id>', include('list.urls')),
    path('list/wishList/None', include('list.urls')),
    path('list/viewItem/addtoWishList/', include('list.urls')),
    # path('login/', include('login.urls')),
    path('', include("django.contrib.auth.urls")),
    path('profile/', include('login.urls')),
    path('editItem/', include('editItem.urls')),
    path('editItem/item',include('editItem.urls')),
    path('profile/delete_account/', include('login.urls')),
    path('editItem/<int:id>', include('editItem.urls')),
    path('editItem/removeItem/<int:id>', include('editItem.urls')),
    path('userWList/', include('userWList.urls')),
    path('api/', include('apiapp.urls')),
    path('makeItem/', include('makeItem.urls')),
]
