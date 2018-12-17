from django import forms
from .models import User, Game, Playerstats


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('my_team', 'game_date', 'venue', 'weather', 'opponent_team', 'my_score', 'opponent_score',)


    #my_team = forms.CharField(label='チーム名')
    #opponent_team = forms.CharField(label='相手チーム名')
    #my_score = forms.IntegerField(label='自得点')
    #opponent_score = forms.IntegerField(label='相手得点')
