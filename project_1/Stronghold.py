class castle:
    def __init__(self, hp=100, elixir=2) -> None:
        self.hp = hp
        self.elixir = elixir
   
    def __str__(self):
        return f"castle: HP={self.hp}, elixir={self.elixir}"