class Player:
    player_count = 0
    def __init__ (self, name=None):
        Player.player_count += 1
        self.number = Player.player_count
        self.name = name if name else f"Player {self.number}"
