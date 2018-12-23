from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    game_date = models.DateTimeField('試合日時')
    venue = models.CharField(max_length=20, blank=True, null=True) #グランド名
    weather = models.CharField(max_length=10, blank=True, null=True) #天気
    my_team = models.CharField(max_length=20, blank=True, null=True) #自チーム名
    opponent_team = models.CharField(max_length=20, blank=True, null=True) #敵チーム名
    my_score = models.IntegerField(blank=True, null=True) #自得点
    opponent_score = models.IntegerField(blank=True, null=True) #敵得点
    inning_score = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.my_team


class Playerstats(models.Model):
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    daseki = models.IntegerField(blank=True, null=True)
    dasuu = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    Walk = models.IntegerField(blank=True, null=True)
    stlike_out = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    dajun = models.IntegerField(blank=True, null=True)
    starting_member = models.BooleanField(default=False)

