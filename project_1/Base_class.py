class hero:
    def __init__(self, hp, armor, dmg, elixir) -> None:
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.elixir = elixir


    def __str__(self):
        return f"{self.__class__}: HP={self.hp}, Armor={self.armor}, Damage={self.dmg}"