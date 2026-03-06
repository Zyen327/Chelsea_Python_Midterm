import csv
import os

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, "players.csv")

def read_players():
    players = []
    try:
        with open(FILENAME) as file:
            for line in file:
                name, pos, ab, hits = line.strip().split(",")
                players.append({
                    "name": name,
                    "position": pos,
                    "at_bats": int(ab),
                    "hits": int(hits)
                })
    except FileNotFoundError:
        print("players.csv not found. Starting with empty lineup.")
    return players


def write_players(players):
    with open(FILENAME, "w") as file:
        for p in players:
            file.write(f"{p['name']},{p['position']},{p['at_bats']},{p['hits']}\n")
