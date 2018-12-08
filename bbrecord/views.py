from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Game
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def index(request):
    return render(request, 'bbrecord/index.html')


def game_list(request):
    games = Game.objects.all()
    return render(request, 'bbrecord/game_list.html', {'games': games})