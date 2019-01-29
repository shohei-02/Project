from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    game_date = models.DateTimeField('試合日時')
    venue = models.CharField(max_length=20, blank=True, null=True) #グランド名
    weather = models.IntegerField(blank=True, null=True) #天気
    top_team = models.CharField(max_length=20, blank=True, null=True) #先行チーム名
    bot_team = models.CharField(max_length=20, blank=True, null=True) #後攻チーム名
    top_score = models.IntegerField(blank=True, null=True) #先行得点
    bot_score = models.IntegerField(blank=True, null=True) #後攻得点
    top_inning_score = models.CharField(max_length=200, blank=True, null=True) #先行イニング得点
    bot_inning_score = models.CharField(max_length=200, blank=True, null=True) #後攻イニング得点
    x_flag = models.BooleanField(default=False) #xフラグ

    def __str__(self):
        return self.top_team


class Playerstats(models.Model):
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    daseki = models.IntegerField(blank=True, null=True)
    dasuu = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    Walk = models.IntegerField(blank=True, null=True)
    stlike_out = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    dajun = models.IntegerField(blank=True, null=True)
    starting_member = models.BooleanField(default=False)
