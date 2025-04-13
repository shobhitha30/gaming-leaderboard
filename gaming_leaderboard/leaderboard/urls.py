from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-player/', views.add_player, name='add_player'),
    path('add-game/', views.add_game, name='add_game'),
    path('update-scores/', views.update_scores, name='update_scores'),
    path('leaderboard/', views.leaderboard_home, name='leaderboard_home'),
    path('leaderboard/<int:game_id>/', views.game_leaderboard, name='game_leaderboard'),
]
