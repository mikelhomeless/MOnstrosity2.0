from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("This is the main page.  It should probably do something")

# Main hub for the players? I think this might be the most used
# Not sure what info will be in here yet.  Right now just a list of 10 players with a link to each player's individual page
def players(request):
    player_list = Player.objects.all()[:10]
    context = {'player_list': player_list}
    return render(request, 'nba/players.html', context)

# A view for each player
def player(request, player_id):
    player = Player.objects.get(playerid=player_id)
    return HttpResponse("{}".format(player))

# Main hub for the games?
# Not sure what info will be in here yet.  Right now just a list of 10 games with a link to each game's individual page
def games(request):
    game_list = Game.objects.all()[:10]
    context = {'game_list': game_list}
    return render(request, 'nba/games.html', context)

# A view for each game
def game(request, game_id):
    game = Game.objects.get(gameid=game_id)
    return HttpResponse("{}".format(game))

# Main hub for the teams?
# Not sure what info will be in here yet.  Right now just a list of all the teams with a link to each teams's individual page
def teams(request):
    team_list = Team.objects.all()
    context = {'team_list': team_list}
    return render(request, 'nba/teams.html', context)

# A view for each game
def team(request, team_name):
    team = Team.objects.get(teamname=team_name)
    return HttpResponse("{}".format(team))