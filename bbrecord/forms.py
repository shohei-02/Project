from django import forms
from .models import User, Game, Playerstats

FIELD_NAME_MAPPING = {
    # 'Modelクラスのフィールド名' : 'name属性の値'
    'field1': 'html_field1',
    'field2': 'html_field2'
}


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = (
            'top_team',
            'game_date',
            'venue',
            'weather',
            'bot_team',
            'top_score',
            'bot_score')
        labels = {
            'top_team': 'チーム名',
            'game_date': '試合日時',
            'venue': '場所',
            'weather': '天気',
            'bot_team': '相手チーム名',
            'top_score': '自チーム得点',
            'bot_score': '相手チーム得点'}

    def add_prefix(self, field_name):  # dict に存在しない場合はフィールド名を利用する
        return super(GameForm, self).add_prefix(field_name)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name',)


class PlayerstatsForm(forms.ModelForm):

    class Meta:
        model = Playerstats
        fields = (
            'player_id',
            'game_id',
            'daseki',
            'dasuu',
            'hit',
            'Walk',
            'stlike_out',
            'position',
            'dajun',
            'starting_member')
        labels = {
            'player_id': '選手名',
            'game_id': 'game_id',
            'daseki': '打席数',
            'dasuu': '打数',
            'hit': '安打',
            'Walk': '四死球',
            'stlike_out': '三振',
            'position': 'ポジション',
            'dajun': '打順',
            'starting_member': 'スタメン'}

    def add_prefix(self, field_name):  # dict に存在しない場合はフィールド名を利用する
        return super(PlayerstatsForm, self).add_prefix(field_name)

