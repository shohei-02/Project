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
    game = Game.objects.get(id=id)
    my_inning = game.my_inning_score.strip("[""]"" ").replace("'", "").split(",")
    opponent_inning = game.opponent_inning_score.strip("[""]"" ").replace("'", "").split(",")
    my_inning = filter(lambda a: a != " ", my_inning)
    opponent_inning = filter(lambda a: a != " ", opponent_inning)
    players = Playerstats.objects.filter(game_id=id).order_by('dajun')
    return render(request, 'bbrecord/game_detail.html', {
        'players': players,
        'games': games,
        'my_inning': my_inning,
        'opponent_inning': opponent_inning})


def game_new(request):
    users = User.objects.all()
    if request.method == "POST":
        a = request.POST
        b = dict(a)
        game = Game.objects.create(
            my_team=a['my_team'],
            game_date=a['game_date'],
            venue=a['venue'],
            weather=a['weather'],
            opponent_team=a['opponent_team'],
            my_score=a['my_score'],
            opponent_score=a['opponent_score'],
            my_inning_score=b['my_inning'],
            opponent_inning_score=b['opponent_inning'])
        game = Game.objects.get(id=game.id)
        for i in range(0, 9):
            player = User.objects.get(name=a.getlist('player_id')[i])
            Playerstats.objects.create(player_id=player,
                                       game_id=game,
                                       dajun=a.getlist('dajun')[i],
                                       daseki=a.getlist('daseki')[i],
                                       dasuu=a.getlist('dasuu')[i],
                                       hit=a.getlist('hit')[i],
                                       Walk=a.getlist('Walk')[i],
                                       stlike_out=a.getlist('stlike_out')[i],
                                       position=a.getlist('position')[i])

        return redirect('game_list')
    return render(request, 'bbrecord/game_edit.html', {'users': users})


def game_delete(request, id):
    game = Game.objects.get(id=id)
    game.delete()
    return redirect('game_list')


