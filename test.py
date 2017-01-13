#testfile

from Player import *
from MancalaGUI import *
from MancalaBoard import *
from TicTacToe import *

execfile("MancalaGUI.py")
p1 = Player(1, Player.HUMAN)
p2 = MancalaPlayer(2, MancalaPlayer.CUSTOM, 6)
startGame(p1, p2)