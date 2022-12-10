from BackgroundView import BackgroundView
from HandView import HandView
from PlayerView import PlayerView
from BettingView import BettingView
from WinnerView import WinnerView

class ViewInterface:

    def __init__(self):
        self.__bg = BackgroundView()
        self.__hv = HandView()
        self.__pv = PlayerView()
        self.__bv = BettingView()
        self.__wv = WinnerView()

    def display_background(self):
        self.__bg.display_background()

    def display_menu(self, actions: [str] = ("EXIT", "DIE", "CALL", "HALF")):
        self.__bg.display_menu(actions)

    def display_rounds(self, rounds: int = 1):
        self.__bg.display_rounds(rounds)

    def display_input(self) -> int:
        self.__bg.display_input()

    def display_hand(self, player: int, hand: dict = (0, 0), front: bool = True):
        self.__hv.display_hand(player, hand, front)

    def display_player(self, player: int, stakes: int = 0):
        self.__pv.display_player(player, stakes)

    def display_betting(self, money: int):
        self.__bv.display_betting(money)

    def display_total_betting(self, money: int):
        self.__bv.display_total_betting(money)

    def display_winner(self, winner: int):
        self.__wv.display_winner(winner)


#sample code
screen = ViewInterface()

screen.display_background()
screen.display_menu()
screen.display_rounds(1)

screen.display_hand(0, (3, 7))
screen.display_hand(1, front=False)
screen.display_player(0, 100000)
screen.display_player(1)
screen.display_betting(10000)
screen.display_total_betting(0)

n = screen.display_input()

screen.display_winner(0)