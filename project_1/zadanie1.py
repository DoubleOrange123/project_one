class hero:
    def __init__(self, hp, armor, dmg) -> None:
        self.hp = hp
        self.armor = armor
        self.dmg = dmg

    def __str__(self):
        return f"Hero: HP={self.hp}, Armor={self.armor}, Damage={self.dmg}"


class swordsman:
    def __init__(self, hp=110, armor=10, dmg=10, armor_stack=2) -> None:
        super().__init__(hp, armor, dmg)
        self.armor_stack = armor_stack

    def __str__(self):
        return f"Swordsman: HP={self.hp}, Armor={self.armor}, Damage={self.dmg}, Armor stack={self.armor_stack}"
    

class knight:
    def __init__(self, hp=120, armor=15, dmg=10, armor_stack=3, bleed = 2) -> None:
        super().__init__(hp, armor, dmg, armor_stack)
        self.bleed = bleed


class archer:
    def __init__(self, hp=90, armor=5, dmg=20, dodge=2, crit_chance = 5) -> None:
        super().__init__(hp, armor, dmg)
        self.dodge = dodge
        self.crit_chance = crit_chance

class priest:
    def __init__(self, hp=130, armor=10, dmg=10, burn=2, self_heal = 10, ally_heal = 15) -> None:
        super().__init__(hp, armor, dmg)
        self.burn = burn
        self.self_heal = self_heal
        self.ally_heal = ally_heal


        