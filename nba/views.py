from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    context = {}
    return render(request, 'nba/index.html', context)


# Main hub for the players? I think this might be the most used
# Not sure what info will be in here yet.  Right now just a list of 10 players with a link to each player's individual page
def players(request):
    player_list = Player.objects.all().order_by('lastname')

    # paginate the results
    paginator = Paginator(player_list, 20)
    page = request.GET.get('page')
    players = paginator.get_page(page)

    context = {'players': players}
    return render(request, 'nba/players.html', context)

# A view for each player
def player(request, player_id):
    player = Player.objects.get(playerid=player_id)    

    # List all of the games, 10 at a time
    games_list = player.playergamestat_set.order_by('-gameid__date')
    paginator = Paginator(games_list, 10)
    page = request.GET.get('page')
    games = paginator.get_page(page)

    # List each season with the average stats

    # Find the distinct seasons.  There has to be a better way but I don't care enough anymore to try to find it
    seasons = games_list.order_by().values_list('gameid__seasonid').distinct()
    seasons = [item for sublist in seasons for item in sublist] #Flatten the list

    season_stats = {}

    for season in seasons:
        games_stats_list = player.playergamestat_set.filter(gameid__in=Game.objects.filter(seasonid=season))

        season_stats[season] = {}
        season_stats[season]['season'] = Season.objects.get(seasonid=season)
        season_stats[season]['team'] = games_stats_list.first().playerteam
        season_stats[season]['games_played'] = len(games_stats_list)
        season_stats[season]['fgm'] = round(games_stats_list.aggregate(Avg('fgm'))['fgm__avg'], 2)
        season_stats[season]['fga'] = round(games_stats_list.aggregate(Avg('fga'))['fga__avg'], 2)
        season_stats[season]['tpm'] = round(games_stats_list.aggregate(Avg('tpm'))['tpm__avg'], 2)
        season_stats[season]['tpa'] = round(games_stats_list.aggregate(Avg('tpa'))['tpa__avg'], 2)
        season_stats[season]['ftm'] = round(games_stats_list.aggregate(Avg('ftm'))['ftm__avg'], 2)
        season_stats[season]['fta'] = round(games_stats_list.aggregate(Avg('fta'))['fta__avg'], 2)
        season_stats[season]['orb'] = round(games_stats_list.aggregate(Avg('orb'))['orb__avg'], 2)
        season_stats[season]['drb'] = round(games_stats_list.aggregate(Avg('drb'))['drb__avg'], 2)
        season_stats[season]['ast'] = round(games_stats_list.aggregate(Avg('ast'))['ast__avg'], 2)
        season_stats[season]['stl'] = round(games_stats_list.aggregate(Avg('stl'))['stl__avg'], 2)
        season_stats[season]['blk'] = round(games_stats_list.aggregate(Avg('blk'))['blk__avg'], 2)
        season_stats[season]['to'] = round(games_stats_list.aggregate(Avg('to'))['to__avg'], 2)
        season_stats[season]['pf'] = round(games_stats_list.aggregate(Avg('pf'))['pf__avg'], 2)
    
    context = {
        'player': player,
        'games': games,
        'season_stats': season_stats
        }
    return render(request, 'nba/player.html', context)

# Main hub for the games?
# Not sure what info will be in here yet.  Right now just a list of 10 games with a link to each game's individual page
def games(request):
    games_list = Game.objects.all().order_by('-date')

    # paginate the results
    paginator = Paginator(games_list, 20)
    page = request.GET.get('page')
    games = paginator.get_page(page)

    context = {'games': games}
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
