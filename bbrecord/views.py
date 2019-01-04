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
    users = User.objects.all()
    if request.method == "POST":
        a = request.POST.dict()
        game = Game.objects.create(
            my_team=a['my_team'],
            game_date=a['game_date'],
            venue=a['venue'],
            weather=a['weather'],
            opponent_team=a['opponent_team'],
            my_score=a['my_score'],
            opponent_score=a['opponent_score'])
        game = Game.objects.get(id=game.id)
        player = User.objects.get(name=a['player_id'])
        Playerstats.objects.create(player_id=player,
                                   game_id=game,
                                   dajun=a['dajun'],
                                   daseki=a['daseki'],
                                   dasuu=a['dasuu'],
                                   hit=a['hit'],
                                   Walk=a['Walk'],
                                   stlike_out=a['stlike_out'],
                                   position=a['position'])
        return redirect('game_list')
    else:
        gform = GameForm()
    return render(request, 'bbrecord/game_edit.html', {'gform': gform, 'users': users})


def game_delete(request, id):
    game = Game.objects.get(id=id)
    game.delete()
    return redirect('game_list')


