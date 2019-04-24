from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .models.hero import Hero


def deny_access_user_with_hero(function):
    def wrapper(request, *args, **kwargs):
        heroes = Hero.objects.filter(user=request.user)
        if heroes:
            return HttpResponseRedirect(reverse('hero:main'))
        return function(request, *args, **kwargs)
    return wrapper


def hero_required(function):
    def wrapper(request, *args, **kwargs):
        heroes = Hero.objects.filter(user=request.user)
        if not heroes:
            return HttpResponseRedirect(reverse('hero:hero_create'))
        return function(request, *args, **kwargs)
    return wrapper
