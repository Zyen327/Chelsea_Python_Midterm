class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_avg(self):
        if self.at_bats == 0:
            return 0.0
        return self.hits / self.at_bats


class Lineup:
    def __init__(self):
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    def remove_player(self, index):
        return self._players.pop(index)

    def move_player(self, old_index, new_index):
        player = self._players.pop(old_index)
        self._players.insert(new_index, player)

    def edit_position(self, index, new_pos):
        self._players[index].position = new_pos

    def edit_stats(self, index, at_bats, hits):
        self._players[index].at_bats = at_bats
        self._players[index].hits = hits

    def get_player(self, index):
        return self._players[index]

    def __len__(self):
        return len(self._players)

    def __iter__(self):
        return iter(self._players)
