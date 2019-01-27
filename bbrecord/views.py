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
    game = Game.objects.get(id=id)
    top_inning_dict = json.loads(game.top_inning_score)
    bot_inning_dict = json.loads(game.bot_inning_score)
    players = Playerstats.objects.filter(game_id=id).order_by('dajun')
    position_dict = {1: "ピッチャー",
                     2: "キャッチャー",
                     3: "ファースト",
                     4: "セカンド",
                     5: "サード",
                     6: "ショート",
                     7: "レフト",
                     8: "センター",
                     9: "ライト"}
    top_inning_dict_2 = [v for i, v in top_inning_dict.items() if not i == 'total' and not v == '']
    bot_inning_dict_2 = [v for i, v in bot_inning_dict.items() if not i == 'total' and not v == '']
    inning = [i for i, v in top_inning_dict.items() if not i == 'total' and not v == '']
    return render(request, 'bbrecord/game_detail.html', {
        'players': players,
        'game': game,
        'top_inning_dict_2': top_inning_dict_2,
        'bot_inning_dict_2': bot_inning_dict_2,
        'inning': inning,
        'position_dict': position_dict})


def game_new(request):
    users = User.objects.all()
    if request.method == "POST":
        a = request.POST
        b = dict(a)
        top_score_list = [int(i) for i in b['top_inning'] if not i == '']
        bot_score_list = [int(i) for i in b['bot_inning'] if not i == '']
        inning = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        top_score_dict = dict(zip(inning, top_score_list))
        bot_score_dict = dict(zip(inning, bot_score_list))
        top_score_dict['total'] = sum(top_score_list)
        bot_score_dict['total'] = sum(bot_score_list)
        top_str = json.dumps(top_score_dict)
        bot_str = json.dumps(bot_score_dict)
        game = Game.objects.create(
            top_team=a['top_team'],
            bot_team=a['bot_team'],
            game_date=a['game_date'],
            venue=a['venue'],
            weather=a['weather'],
            top_score=top_score_dict['total'],
            bot_score=bot_score_dict['total'],
            top_inning_score=top_str,
            bot_inning_score=bot_str)
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
    return render(request, 'bbrecord/game_new.html', {'users': users})


def game_edit(request, id):
    users = User.objects.all()
    game = Game.objects.get(id=id)
    players = Playerstats.objects.filter(game_id=game.id)
    for i in players:
        i.user_name = i.player_id
    top_inning_dict = json.loads(game.top_inning_score)
    bot_inning_dict = json.loads(game.bot_inning_score)
    top_inning_dict_2 = [v for i, v in top_inning_dict.items() if not i == 'total' and not v == '']
    bot_inning_dict_2 = [v for i, v in bot_inning_dict.items() if not i == 'total' and not v == '']
    if request.method == "POST":
        a = request.POST
        b = dict(a)
        top_score_list = [int(i) for i in b['top_inning'] if not i == '']
        bot_score_list = [int(i) for i in b['bot_inning'] if not i == '']
        inning = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        top_score_dict = dict(zip(inning, top_score_list))
        bot_score_dict = dict(zip(inning, bot_score_list))
        top_score_dict['total'] = sum(top_score_list)
        bot_score_dict['total'] = sum(bot_score_list)
        top_str = json.dumps(top_score_dict)
        bot_str = json.dumps(bot_score_dict)
        Game.objects.filter(id=game.id).update(
            top_team=a['top_team'],
            bot_team=a['bot_team'],
            game_date=a['game_date'],
            venue=a['venue'],
            weather=a['weather'],
            top_score=top_score_dict['total'],
            bot_score=bot_score_dict['total'],
            top_inning_score=top_str,
            bot_inning_score=bot_str)
        for i in range(0, 9):
            player = User.objects.get(name=a.getlist('player_id')[i])
            Playerstats.objects.filter(player_id=player, game_id=id).update(
                dajun=a.getlist('dajun')[i],
                daseki=a.getlist('daseki')[i],
                dasuu=a.getlist('dasuu')[i],
                hit=a.getlist('hit')[i],
                Walk=a.getlist('Walk')[i],
                stlike_out=a.getlist('stlike_out')[i],
                position=a.getlist('position')[i])
        return redirect('game_list')
    return render(request, 'bbrecord/game_edit.html', {
        'game': game,
        'users': users,
        'players': players,
        'top_inning_dict_2': top_inning_dict_2,
        'bot_inning_dict_2': bot_inning_dict_2})


def game_delete(request, id):
    game = Game.objects.get(id=id)
    game.delete()
    return redirect('game_list')


