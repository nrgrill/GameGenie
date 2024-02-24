class Player:
    def __init__(self, name='Default Name'):
        self.partners = []
        self.opponents = []
        self.name = name

    def __repr__(self):
        return f'Player(name={self.name})'
    
class Game:
    def __init__(self, id=0):
        self.id = id
        self.team1 = []
        self.team2 = []

def create_tournament(num_players=12, num_games=10, names=[]):
    if not names:
        names = [f'Player {i}' for i in range(1, num_players+1)]
    
    players = []

    for name in names:
        players.append(Player(name))

    for id in range(num_games):
        game = Game(id=id)
    
        game.team1 = []
        game.team2 = []



    

create_tournament()