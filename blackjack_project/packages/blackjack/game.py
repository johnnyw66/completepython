from packages.blackjack.deck import Deck
from packages.blackjack.player import HumanPlayer
from packages.blackjack.player import ComputerPlayer
from packages.blackjack.player import Dealer
from packages.blackjack.blackjackcard import BlackJackCard
from packages.blackjack.card import Card
from packages.blackjack.prompt import Prompt


from time import sleep as sleep

class Game():
	BET_AMOUNT = 10
	DEALERBET_FACTOR = 2.0


	def log(msg, delay = 3):
		print(f"{msg}")
		sleep(3)
		#pass

	def __init__(self, player_type = 'player'):
		self.finished = True
		self.deck = Deck(52)
		self.player = ComputerPlayer("Computer Johnny") if player_type == 'computer' else HumanPlayer("Human Johnny")
		self.dealer = Dealer("Computer Dealer")

	def init(self):
		self.finished = False
		self.shuffle()
		self.player.add(self.deck.deal(2))
		self.dealer.add(self.deck.deal(2))

	def return_cards_to_deck(self):
		player = self.player
		dealer = self.dealer
		deck = self.deck
		deck.return_cards(player.retrieve_cards())
		deck.return_cards(dealer.retrieve_cards())

	def shuffle(self):
		#print("Deck Shuffle")
		self.deck.shuffle()

	def hitxxx(self, player):
		playerhand = player.hand
		dealt = self.deck.deal(1)
		player.add(dealt)
		#return dealt[-1]


	def play(self):
		Game.log("playing game")
		player = self.player
		dealer = self.dealer

		Game.log(f"{player}")
		Game.log(f"{dealer}")

		player_bet = player.placebet(Game.BET_AMOUNT)
		dealer_bet = dealer.placebet(player_bet * Game.DEALERBET_FACTOR)
		gamepot = player_bet + dealer_bet

		Game.log(f"Starting Hand. Player Bets ${player_bet} Dealer Bets ${dealer_bet}. Game Pot at ${gamepot} ")

		self.display_hands()

		player_score = self.players_turn()

		# dealers Turn

		if (player_score > 21):
			# Player BUST -DEALER WIN
			dealer.winbet(gamepot)
			Game.log(f"**** PLAYER BUST **** DEALER WINS {player_score}")

		else:
			Game.log(f"DEALERS TURN -- THE BIG REVEAL -- PLAYER STICKS ON {player_score} ")
			self.display_hands(True)

			dealer_score = self.dealers_turn()

			Game.log(f"----- DEALER STICKS ON {dealer_score} ")

			if (dealer_score > 21):
				# Dealer BUST Player WIN
				player.winbet(gamepot)
				Game.log("**** DEALER BUST **** PLAYER WINS")

			elif (dealer_score > player_score):
				# Dealer WIN (better score)
				dealer.winbet(gamepot)
				Game.log(f"DEALER WINS DEALER: {dealer_score} PLAYER:{player_score}")

			else:
				# Player WIN (better score)
				player.winbet(gamepot)
				Game.log(f"PLAYER WINS PLAYER:{player_score} DEALER: {dealer_score}")


		# Game Finished Reveal all cards
		self.display_hands(True)
		Game.log(f"PLAYER'S POT: ${player.wallet} DEALER'S POT: ${dealer.wallet}")


		if (player.wallet * dealer.wallet < 0.01):
			raise Exception('No Money Left')



	def dealers_turn(self):
		dealer = self.dealer
		return dealer.turn(self.deck, self.player, self.calc_score, self.display_hands)


	#def dealers_turn(self, opponent_cards):

	#	score = BlackJackCard.calc_score(opponent_cards)

	#	Game.log(f"DEALERS TURN Target Score:{target_score} Current Score: {score}")

	#	while (score < target_score and score <= BlackJackCard.HOUSERULES):
	#		#dealt_card =
	#		#Prompt.prompt("Dealer to Hit - Press return to continue", str, [''])
	#		#sleep(3)
	#		self.hit(dealer)
	#		dealt_card = dealer.last_card()
	#		score = self.calc_score(dealer)

	#		Game.log(f"***DEALER HITS*** Card {Card.describe(dealt_card)} current score {score}")
	#		self.display_hands(True)
			#sleep(3)
	#
	#	Game.log(f"***DEALER FINISHES*** Score of {score}")
	#	return score


	def players_turn(self):
		player = self.player
		return player.turn(self.deck, self.dealer, self.calc_score, self.display_hands)

#	def players_turn(self):
#		player = self.player
#		while True:
#			response = self.prompt_input("Hit or Stick?",str,['h','s'])
#			if (response == 's'):
#				return self.calc_score(player)
#			else:
#				self.hit(player)
#				score = self.calc_score(player)
#				self.display_hands()
#				sleep(1)
#				if (score > 21):
#					return score



	def display_hands(self, reveal_all = False):
		player = self.player
		dealer = self.dealer
		#print(f"Dealer : --> {dealer}")
		#print(f"Player : --> {player}")
		#print(f"Reveal All : --> {reveal_all}")

		player_hand_details = self.build_card_display(player)
		dealer_hand_details = self.build_card_display(dealer)

		self.display("Player", player_hand_details, self.calc_score(player))
		self.display(f"Dealer reveal_all={reveal_all}", dealer_hand_details, self.calc_score(dealer), reveal_all)
#		self.display(f"Actual Dealer Cards (Debug)", dealer_hand_details, self.calc_score(dealer), True)

	def display_deck(self):
		deck = self.deck
		deck_details = BlackJackCard.build_card_details(deck.get_cards())
		#print(f"Deck {deck}")

#({'suit': 'Hearts', 'values': 5, 'rank': 'Five'}, {'suit': 'Diamonds', 'values': 11, 'rank': 'Ace'}, {'suit': 'Hearts', 'values': 8, 'rank': 'Eight'})

	def display(self,title, details, actual_score, reveal_all = True):
		revealed_hand = details['hand'] if reveal_all else details['hand'][:-1]
		revealed_score = actual_score if reveal_all else sum([item['values'] for item in revealed_hand])
		rhand_str = "\n".join([f"{item['rank']} of {item['suit']}" for item in revealed_hand])
		Game.log(f"***{title} Cards***\n{rhand_str}\nrevealed score : {revealed_score}, actual Score {actual_score}")
#		print(f"{details}")

	def calc_score(self, player):
		playerhand = player.hand
		return BlackJackCard.calc_score(playerhand.cards)

	def build_card_display(self,player):
		playerhand = player.hand
		return {'score': self.calc_score(player), 'hand' : BlackJackCard.build_card_details(playerhand.cards)}



	def __str__(self):
		return f"Game : {self.player},\n{self.dealer},\n{self.deck}"
