from Base_class import hero

class swordsman(hero):
    def __init__(self, hp=110, armor=10, dmg=10, armor_stack=2, elixir = 8) -> None:
        super().__init__(hp, armor, dmg, elixir)
        self.armor_stack = armor_stack

    def __str__(self):
        return super().__str__ + f", Armor stack={self.armor_stack}"
    

class knight(swordsman):
    def __init__(self, hp=120, armor=15, dmg=10, armor_stack=3, bleed = 2, elixir = 9) -> None:
        super().__init__(hp, armor, dmg, armor_stack, elixir)
        self.bleed = bleed
    
    def __str__(self):
        return super().__str__ + f", Bleed ={self.bleed}"