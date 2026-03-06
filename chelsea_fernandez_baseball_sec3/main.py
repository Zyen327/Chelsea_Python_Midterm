import db
from objects import Lineup, Player
import ui


def display_lineup(lineup):
    print("\n   Player                             POS       AB     H     AVG")
    print("-" * 64)
    for i, p in enumerate(lineup, start=1):
        print(f"{i:<3}{p.full_name:<35}{p.position:<8}{p.at_bats:<7}{p.hits:<6}{p.batting_avg:.3f}")
    print()


def main():
    lineup = Lineup()

    for player in db.read_players():
        lineup.add_player(player)

    game_date = ui.get_game_date()

    while True:
        ui.display_title(game_date)
        choice = input("Menu option: ")

        if choice == "1":
            display_lineup(lineup)

        elif choice == "2":
            first = input("First name: ")
            last = input("Last name: ")
            pos = ui.get_position()
            ab, hits = ui.get_stats()
            lineup.add_player(Player(first, last, pos, ab, hits))
            db.write_players(lineup)
            print(f"{first} {last} was added.\n")

        elif choice == "3":
            num = ui.get_int("Number: ")
            if 1 <= num <= len(lineup):
                p = lineup.remove_player(num - 1)
                db.write_players(lineup)
                print(f"{p.full_name} was deleted.\n")
            else:
                print("Invalid lineup number.\n")

        elif choice == "4":
            num = ui.get_int("Current lineup number: ")
            if 1 <= num <= len(lineup):
                p = lineup.get_player(num - 1)
                print(f"{p.full_name} was selected.")
                new_num = ui.get_int("New lineup number: ")
                if 1 <= new_num <= len(lineup) + 1:
                    lineup.move_player(num - 1, new_num - 1)
                    db.write_players(lineup)
                    print(f"{p.full_name} was moved.\n")
                else:
                    print("Invalid new lineup number.\n")
            else:
                print("Invalid lineup number.\n")

        elif choice == "5":
            num = ui.get_int("Lineup number: ")
            if 1 <= num <= len(lineup):
                p = lineup.get_player(num - 1)
                print(f"You selected {p.full_name} POS={p.position}")
                new_pos = ui.get_position()
                lineup.edit_position(num - 1, new_pos)
                db.write_players(lineup)
                print(f"{p.full_name} was updated.\n")
            else:
                print("Invalid lineup number.\n")

        elif choice == "6":
            num = ui.get_int("Lineup number: ")
            if 1 <= num <= len(lineup):
                p = lineup.get_player(num - 1)
                print(f"You selected {p.full_name} AB={p.at_bats} H={p.hits}")
                ab, hits = ui.get_stats()
                lineup.edit_stats(num - 1, ab, hits)
                db.write_players(lineup)
                print(f"{p.full_name} was updated.\n")
            else:
                print("Invalid lineup number.\n")

        elif choice == "7":
            print("Bye!")
            break

        else:
            print("Invalid menu option.\n")


if __name__ == "__main__":
    main()
