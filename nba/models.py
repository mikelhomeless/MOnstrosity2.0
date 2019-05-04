from django.db import models

class Coach(models.Model):
    coachid = models.AutoField(db_column='CoachID', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=45)
    lastname = models.CharField(db_column='LastName', max_length=45)

    class Meta:
        db_table = 'coach'


class CoachTeams(models.Model):
    coachteamid = models.AutoField(db_column='CoachTeamID', primary_key=True)
    coachid = models.ForeignKey(Coach, models.DO_NOTHING, db_column='CoachID')
    teamname = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamName')
    startdate = models.CharField(db_column='StartDate', max_length=10)
    enddate = models.CharField(db_column='EndDate', max_length=10)

    class Meta:
        db_table = 'coach_teams'


class Game(models.Model):
    gameid = models.AutoField(db_column='GameID', primary_key=True)
    date = models.CharField(db_column='Date', max_length=10)
    hometeam = models.ForeignKey('Team', models.DO_NOTHING, db_column='HomeTeam', related_name='home')
    visitingteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='VisitingTeam', related_name='visiting')
    homescore = models.IntegerField(db_column='HomeScore')
    visitingscore = models.IntegerField(db_column='VisitingScore')
    seasonid = models.ForeignKey('Season', models.DO_NOTHING, db_column='SeasonID')

    class Meta:
        db_table = 'game'


class Player(models.Model):
    playerid = models.AutoField(db_column='PlayerID', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=40)
    lastname = models.CharField(db_column='LastName', max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'player'

class PlayerGameStat(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='PlayerID')
    playerteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='PlayerTeam')
    sp = models.IntegerField(db_column='SP')
    fgm = models.IntegerField(db_column='FGM')
    fga = models.IntegerField(db_column='FGA')
    tpm = models.IntegerField(db_column='3PM')
    tpa = models.IntegerField(db_column='3PA')
    ftm = models.IntegerField(db_column='FTM')
    fta = models.IntegerField(db_column='FTA')
    orb = models.IntegerField(db_column='ORB')
    drb = models.IntegerField(db_column='DRB')
    ast = models.IntegerField(db_column='AST')
    stl = models.IntegerField(db_column='STL')
    blk = models.IntegerField(db_column='BLK')
    to = models.IntegerField(db_column='TO')
    pf = models.IntegerField(db_column='PF')
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')

    class Meta:
        db_table = 'player_game_stats'


class PlayerSeason(models.Model):
    playerseasonid = models.AutoField(db_column='PlayerSeasonID', primary_key=True)
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='PlayerID')
    seasonid = models.ForeignKey('Season', models.DO_NOTHING, db_column='SeasonID')
    salary = models.DecimalField(db_column='Salary', max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'player_season'


class Season(models.Model):
    seasonid = models.AutoField(db_column='SeasonID', primary_key=True)
    seasonyears = models.CharField(db_column='SeasonYears', unique=True, max_length=45)

    class Meta:
        db_table = 'season'


class Team(models.Model):
    teamname = models.CharField(db_column='TeamName', primary_key=True, max_length=50)
    city = models.CharField(db_column='City', max_length=50)
    conference = models.CharField(db_column='Conference', max_length=4)
    division = models.CharField(db_column='Division', max_length=9)

    class Meta:
        db_table = 'team'
