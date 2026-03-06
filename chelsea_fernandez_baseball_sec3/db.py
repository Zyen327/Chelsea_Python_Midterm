from objects import Player

FILENAME = "players.csv"

def read_players():
    players = []
    try:
        with open(FILENAME) as file:
            for line in file:
                first, last, pos, ab, hits = line.strip().split(",")
                players.append(Player(first, last, pos, int(ab), int(hits)))
    except FileNotFoundError:
        print("players.csv not found. Starting empty lineup.")
    return players


def write_players(lineup):
    with open(FILENAME, "w") as file:
        for p in lineup:
            file.write(f"{p.first_name},{p.last_name},{p.position},{p.at_bats},{p.hits}\n")
