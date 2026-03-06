import db

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def display_title():
    print("=" * 64)
    print("                   Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print(", ".join(POSITIONS))
    print("=" * 64)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_position():
    while True:
        pos = input("Position: ").upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Try again.")


def get_stats():
    while True:
        at_bats = get_int("At bats: ")
        hits = get_int("Hits: ")

        if at_bats < 0 or hits < 0:
            print("Values cannot be negative.")
        elif hits > at_bats:
            print("Hits cannot be greater than at bats.")
        else:
            return at_bats, hits


def calc_avg(at_bats, hits):
    if at_bats == 0:
        return 0.0
    return round(hits / at_bats, 3)


def display_lineup(players):
    print("\n   Player          POS     AB      H       AVG")
    print("-" * 64)
    for i, p in enumerate(players, start=1):
        avg = calc_avg(p[2], p[3])
        print(f"{i:<3} {p[0]:<15} {p[1]:<6} {p[2]:<7} {p[3]:<7} {avg:.3f}")
    print()


def add_player(players):
    name = input("Name: ")
    position = get_position()
    at_bats, hits = get_stats()

    players.append([name, position, at_bats, hits])
    db.write_players(players)
    print(f"{name} was added.\n")


def remove_player(players):
    num = get_int("Number: ")
    if 1 <= num <= len(players):
        player = players.pop(num - 1)
        db.write_players(players)
        print(f"{player[0]} was deleted.\n")
    else:
        print("Invalid lineup number.\n")


def move_player(players):
    num = get_int("Current lineup number: ")
    if 1 <= num <= len(players):
        player = players.pop(num - 1)
        print(f"{player[0]} was selected.")
        new_num = get_int("New lineup number: ")
        if 1 <= new_num <= len(players) + 1:
            players.insert(new_num - 1, player)
            db.write_players(players)
            print(f"{player[0]} was moved.\n")
        else:
            print("Invalid new lineup number.\n")
    else:
        print("Invalid lineup number.\n")


def edit_position(players):
    num = get_int("Lineup number: ")
    if 1 <= num <= len(players):
        player = players[num - 1]
        print(f"You selected {player[0]} POS={player[1]}")
        player[1] = get_position()
        db.write_players(players)
        print(f"{player[0]} was updated.\n")
    else:
        print("Invalid lineup number.\n")


def edit_stats(players):
    num = get_int("Lineup number: ")
    if 1 <= num <= len(players):
        player = players[num - 1]
        print(f"You selected {player[0]} AB={player[2]} H={player[3]}")
        at_bats, hits = get_stats()
        player[2] = at_bats
        player[3] = hits
        db.write_players(players)
        print(f"{player[0]} was updated.\n")
    else:
        print("Invalid lineup number.\n")


def main():
    players = db.read_players()
    try:
        while True:
            display_title()
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
                print("Invalid menu option. Try again.\n")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")


if __name__ == "__main__":
    main()
