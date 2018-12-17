from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Game, Playerstats, User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import json
from .forms import GameForm


def index(request):
    return render(request, 'bbrecord/index.html')


def game_list(request):
    games = Game.objects.all()
    return render(request, 'bbrecord/game_list.html', {'games': games})


def game_detail(request, id):
    games = Game.objects.filter(id=id)
    players = Playerstats.objects.filter(game_id=id).order_by('dajun')
    return render(request, 'bbrecord/game_detail.html', {'players': players, 'games': games})


def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('game_list', id=game.pk)
    else:
        form = GameForm()
    return render(request, 'bbrecord/game_edit.html', {'form': form})
