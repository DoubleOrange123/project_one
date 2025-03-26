from Hth import knight, swordsman
from range import archer, priest
from Stronghold import castle

AMOUNT = 1

def main():
    player_1 = castle()
    player_2 = castle()
    action(player_1,player_2)

def game_ends(player_1:castle, player_2:castle)->bool:
    if player_1.hp == 0 or player_2.hp == 0:
        return True
    return False

def action(player_1:castle, player_2:castle):
    print('Game start')
    while not game_ends(player_1,player_2): 
        player_1.elixir += AMOUNT
        player_2.elixir += AMOUNT
        print(player_1,player_2)

def buy()->None:
    print('Game on')
    print('Hire') 
    print('Skip')
        



main()



