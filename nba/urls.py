from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players', views.players, name='players'),
    path('players/<int:player_id>', views.player, name='player'),
    path('games', views.games, name='games'),
    path('games/<int:game_id>', views.game, name='game'),
    path('teams', views.teams, name='teams'),
    path('teams/<str:team_name>', views.team, name='team')   
]
