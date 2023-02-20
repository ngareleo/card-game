from System import player , pocker_manager , game_master


""""
    The player should view all their cards
    The player should be able to select many cards to drop   
    The player should be able to categorize the cards 
        
        ::Attacking cards
        ::Defending cards
        ::Game ending cards
        
    The physical UI
        
"""
class main:

    def __init__(self,pocker_man,game_mas):

        self.pocker_man = pocker_man
        self.game_master = game_mas

class animations:
    pass

class card_movement:
    players_cards = []

    def __init__(self,player_cards,):
        self.players_cards = player_cards


    def view_cards(self):
        pass

class card_managment:
    pass

class card_UI:
    pass

gm_player = main(pocker_manager,game_master)

def game_loop_two(crnt_player):
    print(f"{crnt_player.name}Do you want to view your cards")

if __name__ == '__main__':
    print("Mu name is Leo Mwenda ")



