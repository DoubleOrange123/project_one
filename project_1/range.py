from Base_class import hero

class archer(hero):
    def __init__(self, hp=90, armor=5, dmg=20, dodge=2, crit_chance = 5, elixir = 10) -> None:
        super().__init__(hp, armor, dmg, elixir)
        self.dodge = dodge
        self.crit_chance = crit_chance

class priest (hero):
    def __init__(self, hp=130, armor=10, dmg=10, burn=2, self_heal = 10, ally_heal = 15, elixir = 12) -> None:
        super().__init__(hp, armor, dmg, elixir)
        self.burn = burn
        self.self_heal = self_heal
        self.ally_heal = ally_heal
