from django.test import TestCase
from .models import *


class TestPlayer(TestCase):

    def create_person(self):
        Player.objects.create(playerid=1, lastname='last', firstname='first')

    def setUp(self):
        self.create_person()

    def test_can_get_player_by_id(self):
        self.assertIsNotNone(Player.objects.get(playerid=1))

    def test_can_get_last_name(self):
        player = Player.objects.get(playerid=1)
        self.assertEquals(player.firstname, 'first')

    def test_can_get_first_name(self):
        player = Player.objects.get(playerid=1)
        self.assertEquals(player.lastname, 'last')

    def test_str(self):
        player = Player.objects.get(playerid=1)
        self.assertEquals("{}".format(player), 'last, first')


class TestGame(TestCase):

    def create_game(self):
        Game.objects.create(gameid=1, hometeam=Team.objects.create(teamname='MIAMI HEAT'), visitingteam=Team.objects.create(
            teamname='CLEVELAND CAVELIERS'), homescore=100, visitingscore=102, seasonid=Season.objects.create(seasonid=1, seasonyears='2017/2018'))

    def setUp(self):
        self.create_game()

    def test_can_get_game_by_id(self):
        self.assertIsNotNone(Game.objects.get(gameid=1))

    def test_str(self):
        game = Game.objects.get(gameid=1)
        self.assertEquals("{}".format(game), "{}: {} vs. {}".format(game.date, game.hometeam, game.visitingteam))

    def test_can_get_hometeam_from_game(self):
        game = Game.objects.get(gameid=1)
        self.assertIsInstance(game.hometeam, Team)

    def test_can_get_visitingteam_from_game(self):
        game = Game.objects.get(gameid=1)
        self.assertIsInstance(game.visitingteam, Team)

    def test_can_get_season_from_game(self):
        game = Game.objects.get(gameid=1)
        self.assertIsInstance(game.seasonid, Season)

    def test_can_get_homescore_from_game(self):
        game = Game.objects.get(gameid=1)
        self.assertIsNotNone(game.homescore)

    def test_can_get_visitingscore_from_game(self):
        game = Game.objects.get(gameid=1)
        self.assertIsNotNone(game.visitingscore)


class TestSeason(TestCase):

    def create_season(self):
        Season.objects.create(seasonid=67, seasonyears='2017/2018')

    def setUp(self):
        self.create_season()

    def test_can_get_season_by_id(self):
        self.assertIsNotNone(Season.objects.get(seasonid=67))

    def test_str(self):
        season = Season.objects.get(seasonid=67)
        self.assertEquals("{}".format(season), '2017/2018')

    def test_can_get_season_year(self):
        season = Season.objects.get(seasonid=67)
        self.assertEquals(season.seasonyears, '2017/2018')

class TestCoach(TestCase):

    def create_coach(self):
        Coach.objects.create(coachid=1, firstname='first', lastname='last')

    def setUp(self):
        self.create_coach()

    def test_can_get_coach_by_id(self):
        self.assertIsNotNone(Coach.objects.get(coachid=1))

    def test_str(self):
        coach = Coach.objects.get(coachid=1)
        self.assertEquals("{}".format(coach), 'last, first')

    def test_can_get_first_name(self):
        coach = Coach.objects.get(coachid=1)
        self.assertEquals(coach.firstname, 'first')

    def test_can_get_last_name(self):
        coach = Coach.objects.get(coachid=1)
        self.assertEquals(coach.lastname, 'last')

class TestTeam(TestCase):

    def create_team(self):
        Team.objects.create(teamname='PHEONIX SUNS')

    def setUp(self):
        self.create_team()

    def test_can_get_team_by_name(self):
        self.assertIsNotNone(Team.objects.get(teamname='PHEONIX SUNS'))

    def test_str(self):
        team = Team.objects.get(teamname='PHEONIX SUNS')
        self.assertEquals("{}".format(team), 'PHEONIX SUNS')
