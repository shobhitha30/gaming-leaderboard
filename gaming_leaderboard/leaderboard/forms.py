from django import forms
from .models import Player, Game, Score

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['player', 'game', 'score']
