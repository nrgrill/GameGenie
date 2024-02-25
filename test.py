from itertools import combinations

def generate_schedule(num_players, num_rounds):
    """
    Generates a schedule for a euchre tournament.

    Args:
        num_players: The number of players in the tournament.
        num_rounds: The number of rounds in the tournament.

    Returns:
        A list of lists, where each inner list represents a round and contains pairings of players.
    """

    if num_players % 2 != 0:
        raise ValueError("Number of players must be even.")

    # Calculate the minimum number of rounds required to fulfill all requirements
    min_rounds = (num_players - 1) * 2

    if num_rounds < min_rounds:
        raise ValueError(f"Number of rounds cannot be less than {min_rounds}")

    # Create a list of all players
    players = list(range(num_players))

    # Schedule will be stored in a list of rounds
    schedule = []

    # Generate all possible pairings of players
    player_pairs = list(combinations(players, 2))

    # Rotate the players to generate round-robin pairings
    for _ in range(num_rounds):
        round_pairings = []
        for i in range(num_players // 2):
            round_pairings.append((players[i], players[-i - 1]))
        schedule.append(round_pairings)
        players.insert(1, players.pop())

    return schedule

# Example usage
num_players = 8
num_rounds = 10
try:
    schedule = generate_schedule(num_players, num_rounds)
    for round_num, round in enumerate(schedule):
        print(f"Round {round_num + 1}:")
        for pairing in round:
            print(f"- Player {pairing[0]} vs Player {pairing[1]}")
except ValueError as e:
    print(e)