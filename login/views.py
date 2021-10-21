from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import logging


def profile(request):
    return render(request, "login/profile.html")


def delete_account(request):
    context = {}
    if request.method == "POST":
        if request.POST.get('userID'):
            try:
                u = User.objects.get(id=request.POST.get('userID'))
                u.delete()
                context['msg'] = 'The user is deleted.'
                # logger.error("it worked")
                return redirect("/logout")
            except User.DoesNotExist:
                context['msg'] = 'User does not exist.'
                # logger.error("it didn't work 1")
            except Exception as e:
                # logger.error("it didn't work 2")
                context['msg'] = e.message
            return render(request, "/login/delete_account.html", context=context)

    return render(request, "login/delete_account.html", context=context)
