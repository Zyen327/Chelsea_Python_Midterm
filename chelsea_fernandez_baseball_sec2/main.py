import db
from datetime import date, datetime

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def display_title(game_date=None):
    print("=" * 64)
    print("                   Baseball Team Manager\n")
    print(f"CURRENT DATE:    {date.today()}")
    if game_date:
        print(f"GAME DATE:       {game_date}")
        days = (game_date - date.today()).days
        if days > 0:
            print(f"DAYS UNTIL GAME: {days}")
    print("\nMENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program\n")
    print("POSITIONS")
    print(", ".join(POSITIONS))
    print("=" * 64)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    while True:
        pos = input("Position: ").upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position.")


def get_stats():
    while True:
        ab = get_int("At bats: ")
        hits = get_int("Hits: ")
        if ab < 0 or hits < 0:
            print("Values cannot be negative.")
        elif hits > ab:
            print("Hits cannot exceed at bats.")
        else:
            return ab, hits


def batting_avg(p):
    if p["at_bats"] == 0:
        return 0.0
    return p["hits"] / p["at_bats"]


def display_lineup(players):
    print("\n   Player                             POS       AB     H     AVG")
    print("-" * 64)
    for i, p in enumerate(players, start=1):
        avg = batting_avg(p)
        print(f"{i:<3}{p['name']:<35}{p['position']:<8}{p['at_bats']:<7}{p['hits']:<6}{avg:.3f}")
    print()


def add_player(players):
    name = input("Name: ")
    pos = get_position()
    ab, hits = get_stats()
    players.append({
        "name": name,
        "position": pos,
        "at_bats": ab,
        "hits": hits
    })
    db.write_players(players)
    print(f"{name} was added.\n")


def remove_player(players):
    num = get_int("Number: ")
    if 1 <= num <= len(players):
        p = players.pop(num - 1)
        db.write_players(players)
        print(f"{p['name']} was deleted.\n")
    else:
        print("Invalid lineup number.\n")


def move_player(players):
    num = get_int("Current lineup number: ")
    if 1 <= num <= len(players):
        p = players.pop(num - 1)
        print(f"{p['name']} was selected.")
        new_num = get_int("New lineup number: ")
        if 1 <= new_num <= len(players) + 1:
            players.insert(new_num - 1, p)
            db.write_players(players)
            print(f"{p['name']} was moved.\n")
        else:
            print("Invalid new lineup number.\n")
    else:
        print("Invalid lineup number.\n")


def edit_position(players):
    num = get_int("Lineup number: ")
    if 1 <= num <= len(players):
        p = players[num - 1]
        print(f"You selected {p['name']} POS={p['position']}")
        p["position"] = get_position()
        db.write_players(players)
        print(f"{p['name']} was updated.\n")
    else:
        print("Invalid lineup number.\n")


def edit_stats(players):
    num = get_int("Lineup number: ")
    if 1 <= num <= len(players):
        p = players[num - 1]
        print(f"You selected {p['name']} AB={p['at_bats']} H={p['hits']}")
        ab, hits = get_stats()
        p["at_bats"] = ab
        p["hits"] = hits
        db.write_players(players)
        print(f"{p['name']} was updated.\n")
    else:
        print("Invalid lineup number.\n")


def get_game_date():
    user_input = input("Enter game date (YYYY-MM-DD) or press Enter to skip: ")
    if not user_input.strip():
        return None
    try:
        return datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Skipping game date.")
        return None


def main():
    players = db.read_players()
    game_date = get_game_date()

    while True:
        display_title(game_date)
        choice = input("Menu option: ")

        if choice == "1":
            display_lineup(players)
        elif choice == "2":
            add_player(players)
        elif choice == "3":
            remove_player(players)
        elif choice == "4":
            move_player(players)
        elif choice == "5":
            edit_position(players)
        elif choice == "6":
            edit_stats(players)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option.\n")



if __name__ == "__main__":
    main()
