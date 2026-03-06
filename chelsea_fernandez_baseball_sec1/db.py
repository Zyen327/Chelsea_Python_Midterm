import csv
import os

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, "players.csv")

def read_players():
    players = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                position = row[1]
                at_bats = int(row[2])
                hits = int(row[3])
                players.append([name, position, at_bats, hits])
    except FileNotFoundError:
        print("players.csv not found. Starting with an empty lineup.")
    return players


def write_players(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for player in players:
            writer.writerow(player)
