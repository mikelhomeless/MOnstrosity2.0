from django.contrib import admin

from .models import *

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(CoachTeams)
admin.site.register(PlayerGameStat)
admin.site.register(PlayerSeason)
admin.site.register(Season)
admin.site.register(Team)
