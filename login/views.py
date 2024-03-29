from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from database.models import Items
import logging


def profile(request):
    if request.method == "POST":
        if request.POST.get('ID'):
            u = User.objects.get(id=request.POST.get('ID'))
            if request.POST.get('username'):
                u.username = request.POST.get('username')
            if request.POST.get('password'):
                u.set_password(request.POST.get('password'))
            u.save()
            return redirect("/login")
    return render(request, "login/profile.html")



def delete_account(request):
    if request.method == "POST":
        u = User.objects.get(id=request.POST.get('userID'))
        item = Items.objects.all()
        if request.POST.get('password'):
            if u.check_password(request.POST.get('password')):
                u.delete()
                for i in item:
                    if i.userId == u.id:
                        i.delete()
                return redirect("/logout")
        return render(request, "login/delete_account.html", {"msg": "Password Incorrect"})

    return render(request, "login/delete_account.html")
