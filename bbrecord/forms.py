from django import forms
from .models import User, Game, Playerstats


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('my_team', 'game_date', 'venue', 'weather', 'opponent_team', 'my_score', 'opponent_score',)
        labels = {'my_team': 'チーム名', 'game_date': '試合日時', 'venue': '場所', 'weather': '天気',
                  'opponent_team': '相手チーム名', 'my_score': '自チーム得点', 'opponent_score': '相手チーム得点',}


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name',)


class PlayerstatsForm(forms.ModelForm):

    class Meta:
        model = Playerstats
        fields = ('player_id', 'game_id', 'daseki', 'dasuu', 'hit', 'Walk', 'stlike_out', 'position', 'dajun',
                  'starting_member',)
