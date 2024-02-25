from random import choice, randint

class Player:
    """
    Store name, potential partners, and potential opponents.
    """
    def __init__(self, name: str='Default Name'):
        self.name = name
        self.partners = []
        self.opponents = []

    def remove_partner(self, player):
        if player in self.partners:
            self.partners.remove(player)

    def remove_opponents(self, players):
        for player in players:
            if player in self.opponents:
                self.opponents.remove(player)

    def initialize(self, players: list):
        self.partners = [i for i in players if i.name != self.name]
        self.opponents = [i for i in players if i.name != self.name]

    def __repr__(self):
        return f'{type(self).__name__}(name={self.name})'
    
class Table:
    """
    Store table number and each team's players.
    """
    def __init__(self, id: int=0):
        self.id = id
        self.team1 = []
        self.team2 = []

    def set_players(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def __repr__(self):
        return f'{type(self).__name__}(id={self.id}, team1={[p.name for p in self.team1]}, team2={[p.name for p in self.team2]})'
    
    def __str__(self):
        return f'{self.team1[0].name} & {self.team1[1].name} vs. {self.team2[0].name} & {self.team2[1].name}'

class Game:
    """
    Store table settings for each game.
    """
    def __init__(self, tables=[], id=0, untabled_players=[]):
        self.id = id
        self.tables = tables
        self.untabled_players = untabled_players

    def initialize(self, players: list):
        self.untabled_players = [i for i in players]

    def __repr__(self):
        return f'{type(self).__name__}(tables={self.tables})'

def reset_players(players):
    for player in players:
        player.initialize(players)

def create_tournament(num_players=12, num_games=10, names=[]):
    if not names:
        names = [f'Player{i}' for i in range(1, num_players+1)]
    else:
        num_players = len(names)
    
    players = [Player(name) for name in names]
    for player in players:
        player.initialize(players)

    games = []
    for i in range(num_games):
        players = [Player(name) for name in names]
        for player in players:
            player.initialize(players)
        games.append(Game(id=i, untabled_players=players))

    for game in games:
        game.tables = [Table(id=i) for i in range(1, (num_players//4)+1)]

        for table in game.tables:  # 4 players per table    
            if len(game.untabled_players) == 0:
                break    
            player_index = randint(0, len(game.untabled_players) - 1)
            p1 = game.untabled_players[player_index]
            p2 = choice([p for p in game.untabled_players if p.name != p1.name])
            p3 = choice([p for p in game.untabled_players if p.name not in [p1.name, p2.name]])
            p4 = choice([p for p in game.untabled_players if p.name not in [p1.name, p2.name, p3.name]])
            tabled_players = [p1, p2, p3, p4]
            for p in tabled_players:
                game.untabled_players.remove(p)


            # Remove partners and opponents


            # Set up teams
            team1 = [p1, p2]
            team2 = [p3, p4]
            table.set_players(team1, team2)

            
        # After setting up the game, reset players to allow for new combinations
        reset_players(players)

    output = ''
    for i, game in enumerate(games):
        output += f'Game {i+1}\n'
        for table in game.tables:
            output += f'{table}\n'


    return output

if __name__ == '__main__':
    # Example usage
    tournament = create_tournament(names=[i for i in range(12)])

    print(tournament)
