from django.contrib import admin

from .models import *

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass

@admin.register(CoachTeams)
class CoachTeamsAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayerGameStat)
class PlayerGameStatAdmin(admin.ModelAdmin):
    pass

@admin.register(PlayerSeason)
class PlayerSeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
