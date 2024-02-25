import itertools
import random

def generate_schedule(players, num_rounds):
    if len(players) % 4 != 0:
        num_byes = 4 - (len(players) % 4)
        players.extend(['BYE'] * num_byes)

    matches_per_round = len(players) // 4

    schedule = []
    for round_num in range(num_rounds):
        round_schedule = []
        paired_players = set()  # Keep track of paired players in this round
        for match_num in range(matches_per_round):
            team1 = get_unique_pair(players, paired_players)
            team2 = get_unique_pair(players, paired_players)
            round_schedule.append((team1, team2))
        schedule.append(round_schedule)

    return schedule

def get_unique_pair(players, paired_players):
    random.shuffle(players)
    pair = random.sample(players, 2)
    while any(player in paired_players for player in pair):
        random.shuffle(players)
        pair = random.sample(players, 2)
    paired_players.update(pair)
    return pair

def display_schedule(schedule):
    for round_num, matches in enumerate(schedule, 1):
        print(f"Round {round_num}:")
        for match, table_num in zip(matches, range(1, len(matches) + 1)):
            print(f"Table {table_num}")
            print(f"| {match[0][0]} and {match[0][1]} | vs | {match[1][0]} and {match[1][1]} |")
        print()

if __name__ == "__main__":
    num_players = 12 # int(input("Enter the number of players (should be a multiple of 4): "))
    player_names = [i for i in range(num_players)]

    tournament_schedule = generate_schedule(player_names, 10)
    display_schedule(tournament_schedule)
