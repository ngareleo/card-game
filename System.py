from random import choice
from time import sleep


class suit:##To allow card matching

    def __init__(self,identifier):
        self.identifier = identifier
class type:##To allow matching of cards

    def __init__(self,identifier):
        self.identifier = identifier
##Types#########################################
class ace:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "ace"

    def cause_consequence(self):
        pass
class two:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "two"

    def pick_card(self):
        pass


class three:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "three"

    def cause_consequence(self):
        pass

class four:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "four"

    def cause_consequence(self):
        pass


class five:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "five"

    def cause_consequence(self):
        pass
class six:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "six"

    def cause_consequence(self):
        pass
class seven:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "seven"

    def cause_consequence(self):
        pass

class eight:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "eight"

    def cause_consequence(self):
        pass

class nine:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "nine"


    def cause_consequence(self):
        pass

class ten:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "ten"


    def cause_consequence(self):
        pass

class joker:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "joker"


    def cause_consequence(self):
        pass

class king:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "king"


    def cause_consequence(self):
        pass

class queen:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "queen"

    def cause_consequence(self):
        pass

class jack:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "jack"


    def cause_consequence(self):
        pass

####################################################################################################
##Suits
class clubs:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "clubs"
class diamonds:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "diamonds"
class spades:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "spades"
class hearts:

    def __init__(self,identifier = None):
        self.identifier = identifier
        self.identifier = "hearts"

##################################################################
##Game management
class card:
    # The individual_card
    def __init__(self,card_type,card_suit):

        self.card_type = card_type
        self.card_suit = card_suit

    def print_type(self):

        print(f"{self.card_type.identifier.capitalize()} of {self.card_suit.identifier.capitalize()}")

class pocker_manager:
    #Hand out penalties
    #Hands out card to players
    #Shuffles card
    #Decide when game ends when a player ends their stack legally
    def __init__(self, game_manager = None ,players = None ,game_stack=None,tired_stack=None , current_player = None , card_played = None , GD_clockwise = None):

        self.players = list(players)
        self.game_manager = game_manager
        self.game_stack = list(game_stack)
        self.tired_stack = list(tired_stack)
        self.current_player = current_player
        self.card_played = card_played
        self.GD_clockwise = GD_clockwise
        self.GD_clockwise = True

    def make_cards(self):
        total_deck = []
        self.tired_stack = []

        suits = [spades(),hearts(),diamonds(),clubs()]
        types = [ace(),two(),three(),four(),five(),six(),seven(),eight(),nine(),ten(),jack(),queen(),king(),joker()]

        for suit in suits:
            for type in types:
                total_deck.append(card(type,suit))

        self.game_stack = total_deck
    def print_all_cards(self):

        print("\nCards in main stack are :\n")
        for card in self.game_stack:
            card.print_type()

    def split_cards(self):# Happens at the beginning of the game

        for player in self.players:

            split(MS = self.game_stack, PS = player.players_deck, NOC = 4)
            player.deck_manager.number_of_cards = 4
            player.deck_manager.cards = player.players_deck
    def pick_first_player(self):

        random_player = choice(self.players)
        self.current_player = random_player
        random_player.player_call = True
        return random_player

    def check_validity(self):
        pass


    def look_for_consequence(self):
        pass

    def check_end_game(self):
        pass

    """"

    def ask_call(self):

        if not game_end:

            for player in self.players:

                print(f"{space}{player.name.capitalize()} DO YOU WANT TO MAKE CALL ?\n{space}\t")
                sleep(5)
                reply = input(" Yes or No ,y \\ n ")
                if reply == 'y':
                    player.make_call()
                    print(f"{space}{player.name.capitalize()} HAS MADE CALL\n")

    """


############################################ POCKER MASTER CLASS #############################################
class game_info:
    ##  Who made move
    ##  Card added to stack

    pass


class stack_manager:
    ##Controls the 3 stacks
        #1.Tired stack
        #2.Game stack
        #3.Player's stack
    ##  Arrangment
    def __init__(self,number_of_cards = None,cards=None,card_logic=None):
        self.number_of_cards = number_of_cards
        self.card_logic = card_logic
        self.card_logic = cardLogic()
        self.card = cards


class cardLogic:
    pass


class player:
    ##  Must have a stack
    ##  Player must make call to end game
    def __init__(self ,name ,players_deck ,deck_manager, card_played = None , pocker_manager = None ,game_master = None ,penalized = None , call_made = None ,  players_call = None):
        self.players_deck = list(players_deck)
        self.deck_manager = deck_manager
        self.name = str(name).capitalize()
        self.card_played = card_played
        self.pocker_manager = pocker_manager
        self.game_master = game_master
        self.penalized = penalized
        self.penalized = False
        self.call_made = call_made
        self.call_made = False
        self.players_call = players_call
        self.players_call = False

    def play_card(self):

        if self.penalized:
            pass
        else:
            print(f"{space}YOUR CARDS:\n")
            for crd in self.players_deck:
                print(f"{space}{crd.card_type.identifier} of {crd.card_suit.identifier}\n")

    def arrange_cards(self):
        pass

    def make_call(self):
        self.call_made = True
        return self.call_made

###################################################  PLAYER CLASS #########################################################################
space = "\n\t\t\t\t"
game_end = False

class game_master:

    def __init__(self,pocker_manager = None ,game_info = None ,number_of_players=None , players = None , current_player = None):
        self.number_of_players = number_of_players
        self.players = list(players)
        self.pocker_manager = pocker_manager
        self.game_info = game_info
        self.current_player = current_player

    def start_game(self):

        print(f"{space}WELCOME TO OUR GAME OF CARD NIGHT\n\n")
        NOP = input(f"{space}HOW MANY PLAYERS :: ")
        input_correct = False
        while not input_correct: ##To prevent type(NOP) != int
            try:
                input_correct = int(NOP) > 0
            except:
                print(f"{space}Enter number please\n")
                NOP = input(f"{space}HOW MANY PLAYERS :: ")
        self.number_of_players = int(NOP)
        np = 0; name_taken = False; name_null = False
        while ( np < int(NOP)):
            players_deck = []
            deck_mang = stack_manager()
            PN = input(f"{space} PLAYER NAME :: ")
            for pl in self.players:
                if pl.name == str(PN):
                    name_taken = True
            if len(PN) == 0:
                name_null = True
            np += 1
            if name_taken or name_null: #To prevent two players with common name
                if name_taken:
                    print(f"{space}NAME TAKEN\n")
                if name_null:
                    print(f"{space}NAME NULL\n")
                np -= 1
                name_taken = False
                name_null = False
            else:
                self.players.append(player(PN,players_deck=players_deck,deck_manager=deck_mang,game_master=self))

        print(f"{space}{self.number_of_players} players  made successfully")
        for plr in self.players:
            print(f"{space}{plr.name} HAS BEEN ADDED TO GAME ")


    def next_player(self):

        crnt_plr = self.current_player
        gm_players = self.players
        if not game_end:
            if self.pocker_manager.GD_clockwise == True:
                if gm_players.index(crnt_plr) == len(gm_players) - 1:
                    self.current_player = self.players[0]
                    self.pocker_manager.current_player = self.current_player
                else:
                    self.current_player = gm_players[gm_players.index(crnt_plr) + 1]
                    self.pocker_manager.current_player = self.current_player
            else:
                if gm_players.index(crnt_plr) == 0:
                    self.current_player = self.players[-1]
                    self.pocker_manager.current_player = self.current_player
                else:
                    self.current_player = gm_players[gm_players.index(crnt_plr) - 1]
                    self.pocker_manager.current_player = self.current_player

        return crnt_plr

    def feed_player(self):

        for plr in self.players:
            plr.pocker_manager = self.pocker_manager

#################################################################### END OF GAME MASTER CLASS #######################################################################
def split(MS,PS,NOC):
    ##Feed cards to players during game start and penalty giving
    CNC_added_PS = 0
    while CNC_added_PS < NOC:
        random_card = choice(MS)
        PS.append(random_card)
        MS.remove(random_card)
        CNC_added_PS += 1


def shuffle(stack):

    #Shuffles the cards in random
    #Card shuffling  algorithm
    len_of_stack = len(stack)
    cc = 0
    shuffled_stack = []
    while (cc <= len_of_stack - 1):
        random_card = choice(stack)
        shuffled_stack.append(random_card)
        stack.remove(random_card)
        cc += 1
    return shuffled_stack

def setup():
    global GM
    global PM
    GM = game_master(players = [])
    PM = pocker_manager(players = [] ,game_stack = [] ,tired_stack = [])
    PM.game_master = GM
    GM.pocker_manager = PM
    PM.players = GM.players
    GM.start_game()
    PM.make_cards()
    PM.split_cards()
    GM.feed_player()
    PM.pick_first_player()
    PM.GD_clockwise = False
def game_loop():

    while not game_end:
        GM.current_player = PM.current_player
        print(f"Current player is {PM.current_player.name}")
        GM.next_player()
        sleep(4)


####################################  GAME FUNCTIONS ###########################################################
if __name__ == '__main__':
    setup()
    print(GM.current_player)
    game_loop()
