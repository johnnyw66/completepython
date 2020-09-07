#!/usr/bin/env python

from packages.blackjack.game import Game
from packages.blackjack.blackjackcard import BlackJackCard
from packages.tools.logger import Logger

@Logger("",level = 0)
def calcBestScore(lst):
	return 0

#@Logger("LOGINFO",level=0)
#def test2(a,b,c,d):
#	print("test2")

#scores = BlackJackCard.build_hand_scores([0,13,1])

#Logger.log("Hello World")
#test2('my','args','list',666)
#print(f"{scores}\n")
#calcBestScore(scores)

game = Game()
player = game.player
computer = game.dealer
deck = game.deck

game_finished = False
#print(game)
#game.hit(player)
while True:

	game.init()

	try:
		game.play()

	except Exception as e:
		print(f"{e}")
		break
	else:
		print("ELSE STATEMENT")
		game.return_cards_to_deck()
		print(f"{game.deck}")
		Game.log("CARDS RETURNED",3)
	finally:
		print("FINALLY")

print("GAME FINISHED")
