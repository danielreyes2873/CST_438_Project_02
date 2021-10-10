from django.shortcuts import render


def profile(request):
    return render(request, "login/profile.html")
