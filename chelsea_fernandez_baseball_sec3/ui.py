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


def get_game_date():
    user_input = input("Enter game date (YYYY-MM-DD) or press Enter to skip: ")
    if not user_input.strip():
        return None
    try:
        return datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Skipping game date.")
        return None
