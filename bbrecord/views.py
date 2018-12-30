from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Game, Playerstats, User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import json
from .forms import GameForm, PlayerstatsForm


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
        gform = GameForm(request.POST)
        if gform.is_valid():
            game = gform.save(commit=False)
            game.save()
            game = Game.objects.get(id=game.id)
            user = request.POST.getlist('player_id')
            for i in user:
                player = User.objects.get(id=i)
                Playerstats.objects.create(
                    player_id=player,
                    game_id=game,
                # dajun=request.POST['dajun'],
                # daseki=request.POST['daseki'],
                # position=request.POST['position'],
                # dasuu=request.POST['dasuu'],
                # hit=request.POST['hit'],
                # Walk=request.POST['Walk'],
                # stlike_out=request.POST['stlike_out'],
                )
            return redirect('game_list')
    else:
        gform = GameForm()
        pform = PlayerstatsForm()
    return render(request, 'bbrecord/game_edit.html', {'gform': gform, 'pform': pform})


def game_delete(request, id):
    game = Game.objects.get(id=id)
    game.delete()
    return redirect('game_list')


