from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Game, Score
from .forms import PlayerForm, GameForm, ScoreForm
from django.db.models import Avg, Max

# Home Page
def home(request):
    return render(request, 'leaderboard/home.html')

# Add Player
def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'leaderboard/add_player.html', {'form': form})

# Add Game
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'leaderboard/add_game.html', {'form': form})

# Update Scores
def update_scores(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScoreForm()
    return render(request, 'leaderboard/update_scores.html', {'form': form})

# Leaderboard Selection
def leaderboard_home(request):
    games = Game.objects.all()
    return render(request, 'leaderboard/leaderboard_home.html', {'games': games})

# Leaderboard for a Specific Game
def game_leaderboard(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    scores = Score.objects.filter(game=game).order_by('-score')

    ranked_scores = []
    rank = 1
    for i, score in enumerate(scores):
        if i > 0 and scores[i].score < scores[i - 1].score:
            rank = i + 1
        ranked_scores.append({'rank': rank, 'player': score.player.name, 'score': score.score})

    return render(request, 'leaderboard/game_leaderboard.html', {'game': game, 'ranked_scores': ranked_scores})

