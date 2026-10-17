import random


# ---------------------------------
# 1. PERSON
# ---------------------------------

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + " " + self.lastname

    def __lt__(self, other):
        # Önce soyadına, soyadı aynıysa ada göre sıralama yapar.
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname


# ---------------------------------
# 2. PLAYER
# ---------------------------------

class Player(Person):
    player_counter = 1

    def __init__(self, name, lastname):
        super().__init__(name, lastname)

        self.player_id = Player.player_counter
        Player.player_counter += 1

        self.shooting_power = random.randint(4, 8)
        self.points = []
        self.team = None

    def get_id(self):
        return self.player_id

    def get_power(self):
        return self.shooting_power

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def add_to_points(self, points):
        self.points.append(points)

    def get_points(self):
        return sum(self.points)

    def get_points_detailed(self):
        return self.points

    def reset(self):
        self.points = []

    def __lt__(self, other):
        if self.get_points() == other.get_points():
            return super().__lt__(other)
        return self.get_points() < other.get_points()


# ---------------------------------
# 3. MANAGER
# ---------------------------------

class Manager(Person):
    manager_counter = 1

    def __init__(self, name, lastname):
        super().__init__(name, lastname)

        self.manager_id = Manager.manager_counter
        Manager.manager_counter += 1

        self.influence_points = []
        self.team = None

    def get_id(self):
        return self.manager_id

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def add_influence(self, points):
        self.influence_points.append(points)

    def get_influence(self):
        return sum(self.influence_points)

    def get_influence_detailed(self):
        return self.influence_points

    def reset(self):
        self.influence_points = []

    def __lt__(self, other):
        if self.get_influence() == other.get_influence():
            return super().__lt__(other)
        return self.get_influence() < other.get_influence()


# ---------------------------------
# 4. TEAM
# ---------------------------------

class Team:
    def __init__(self, name, manager, players):
        self.name = name
        self.manager = manager
        self.players = players

        self.wins = 0
        self.losses = 0
        self.points_scored = 0
        self.points_conceded = 0
        self.fixtures = []

        manager.set_team(self)

        for player in players:
            player.set_team(self)

    def __str__(self):
        return self.name

    def get_points(self):
        # Her galibiyet 2 lig puanı kazandırır.
        return self.wins * 2

    def add_result(self, scored, conceded):
        self.points_scored += scored
        self.points_conceded += conceded

        if scored > conceded:
            self.wins += 1
        elif scored < conceded:
            self.losses += 1

    def reset(self):
        self.wins = 0
        self.losses = 0
        self.points_scored = 0
        self.points_conceded = 0


# ---------------------------------
# 5. MATCH
# ---------------------------------

class Match:
    def __init__(self, home_team, away_team, week_no):
        self.home_team = home_team
        self.away_team = away_team
        self.week_no = week_no

        self.played = False
        self.home_score = 0
        self.away_score = 0

    def is_played(self):
        return self.played

    def play(self):
        # Oynanmış bir maç tekrar oynanmaz.
        if self.played:
            return

        # Menajerlerin maç öncesi etkisi.
        home_bonus = random.randint(-10, 10)
        away_bonus = random.randint(-10, 10)

        self.home_team.manager.add_influence(home_bonus)
        self.away_team.manager.add_influence(away_bonus)

        self.home_score = home_bonus
        self.away_score = away_bonus

        # Her oyuncunun bu maçtaki puanlarını ayrı ayrı tutarız.
        home_player_points = {}
        away_player_points = {}

        # Normal maç dört periyottur.
        for period in range(4):
            for player in self.home_team.players:
                points = max(0, player.get_power() + random.randint(-5, 5))
                self.home_score += points
                home_player_points[player] = home_player_points.get(player, 0) + points

            for player in self.away_team.players:
                points = max(0, player.get_power() + random.randint(-5, 5))
                self.away_score += points
                away_player_points[player] = away_player_points.get(player, 0) + points

        # Beraberlik varsa uzatma periyodu oynanır.
        while self.home_score == self.away_score:
            for player in self.home_team.players:
                points = max(0, player.get_power() + random.randint(-5, 5))
                self.home_score += points
                home_player_points[player] = home_player_points.get(player, 0) + points

            for player in self.away_team.players:
                points = max(0, player.get_power() + random.randint(-5, 5))
                self.away_score += points
                away_player_points[player] = away_player_points.get(player, 0) + points

        # Her oyuncunun maç puanını listesine ekleriz.
        for player in home_player_points:
            player.add_to_points(home_player_points[player])

        for player in away_player_points:
            player.add_to_points(away_player_points[player])

        # Takım istatistiklerini güncelleriz.
        self.home_team.add_result(self.home_score, self.away_score)
        self.away_team.add_result(self.away_score, self.home_score)

        self.played = True

    def get_match_score(self):
        if not self.played:
            return None
        return (self.home_score, self.away_score)

    def get_teams(self):
        return (self.home_team, self.away_team)

    def get_home_team(self):
        return self.home_team

    def get_away_team(self):
        return self.away_team

    def get_winner(self):
        if not self.played:
            return None

        if self.home_score > self.away_score:
            return self.home_team

        return self.away_team

    def __str__(self):
        if not self.played:
            return str(self.home_team) + " vs. " + str(self.away_team)

        return (str(self.home_team) + " (" + str(self.home_score) + ") vs. (" +
                str(self.away_score) + ") " + str(self.away_team))


# ---------------------------------
# 6. SEASON
# ---------------------------------

class Season:
    def __init__(self):
        self.teams = []
        self.players = []
        self.managers = []
        self.fixture = []
        self.current_week = 1

        # Örnek takım isimleri.
        team_names = [
            "Ankara Falcons",
            "Istanbul Lions",
            "Izmir Waves",
            "Bursa Bulls"
        ]

        # Her takım için bir menajer.
        manager_names = [
            ("Murat", "Yilmaz"),
            ("Selin", "Kaya"),
            ("Deniz", "Demir"),
            ("Ece", "Aydin")
        ]

        # Her takım için beş oyuncu.
        player_names = [
            ("Ali", "Can"), ("Mert", "Arslan"), ("Efe", "Yildiz"),
            ("Can", "Eren"), ("Bora", "Kaplan"),
            ("Emir", "Acar"), ("Kerem", "Aslan"), ("Arda", "Celik"),
            ("Kaan", "Sari"), ("Umut", "Koc"),
            ("Deniz", "Aksoy"), ("Ege", "Kurt"), ("Baran", "Tas"),
            ("Ozan", "Polat"), ("Yigit", "Gunes"),
            ("Cem", "Oz"), ("Onur", "Tekin"), ("Berk", "Inan"),
            ("Tuna", "Isik"), ("Poyraz", "Er")
        ]

        # Takımları, menajerleri ve oyuncuları oluştururuz.
        for i in range(len(team_names)):
            manager_name = manager_names[i]
            manager = Manager(manager_name[0], manager_name[1])
            self.managers.append(manager)

            team_players = []

            for j in range(5):
                player_name = player_names[i * 5 + j]
                player = Player(player_name[0], player_name[1])

                self.players.append(player)
                team_players.append(player)

            team = Team(team_names[i], manager, team_players)
            self.teams.append(team)

        random.shuffle(self.teams)
        self.build_fixture()

    def build_fixture(self):
        self.fixture = []

        for team in self.teams:
            team.fixtures = []

        # Her takım diğer takımlarla bir kez oynar.
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                home_team = self.teams[i]
                away_team = self.teams[j]

                week_no = len(self.fixture) + 1
                match = Match(home_team, away_team, week_no)
                return_match = Match(away_team, home_team, week_no + 1)

                self.fixture.append(match)
                self.fixture.append(return_match)

                home_team.fixtures.append(match)
                away_team.fixtures.append(match)
                home_team.fixtures.append(return_match)
                away_team.fixtures.append(return_match)

    def get_week_fixture(self, week_no):
        if week_no < 1 or week_no > len(self.fixture):
            return None
        return [self.fixture[week_no - 1]]

    def play_week(self):
        if self.current_week > len(self.fixture):
            return

        match = self.fixture[self.current_week - 1]
        match.play()
        self.current_week += 1

        self.players.sort(reverse=True)
        self.managers.sort(reverse=True)
        self.teams.sort(key=lambda team: (team.get_points(), team.points_scored), reverse=True)

    def get_players(self):
        return self.players

    def get_managers(self):
        return self.managers

    def get_teams(self):
        return self.teams

    def get_season_length(self):
        return len(self.fixture)

    def get_best_player(self):
        if not self.players:
            return None
        return max(self.players, key=lambda player: player.get_points())

    def get_best_manager(self):
        if not self.managers:
            return None
        return max(self.managers, key=lambda manager: manager.get_influence())

    def get_most_scoring_team(self):
        if not self.teams:
            return None
        return max(self.teams, key=lambda team: team.points_scored)

    def get_champion(self):
        if self.current_week <= len(self.fixture):
            return None
        if not self.teams:
            return None
        return max(self.teams, key=lambda team: (team.get_points(), team.points_scored))


# ---------------------------------
# PROGRAMI CALISTIR
# ---------------------------------

def main():
    season = Season()

    print("BASKETBALL LEAGUE")
    print("=================")
    print("Takim sayisi:", len(season.get_teams()))
    print("Mac sayisi:", season.get_season_length())
    print()

    # Sezonun bütün maçlarını oynatırız.
    # play_week() maçı oynatır, haftayı ilerletir ve sıralamaları günceller.
    while season.current_week <= season.get_season_length():
        match = season.fixture[season.current_week - 1]
        print("WEEK", season.current_week)
        season.play_week()
        print(match)

    print()
    print("FINAL STANDINGS")

    for team in season.get_teams():
        print(team, "| Lig puani:", team.get_points(),
              "| Galibiyet:", team.wins,
              "| Atilan sayi:", team.points_scored)

    print()
    print("Sampiyon:", season.get_champion())
    print("En cok sayi atan takim:", season.get_most_scoring_team())
    print("En cok puan alan oyuncu:", season.get_best_player())
    print("En yuksek etki puanli menajer:", season.get_best_manager())


if __name__ == "__main__":
    main()
