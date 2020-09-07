from packages.blackjack.deck import Deck
from packages.blackjack.player import Player
from packages.blackjack.player import ComputerPlayer
from packages.blackjack.blackjackcard import BlackJackCard
from packages.blackjack.card import Card

from time import sleep as sleep

class Game():
	HOUSERULES = 21
	BET_AMOUNT = 10
	DEALERBET_FACTOR = 2.0


	def log(msg, delay = 3):
		print(f"{msg}")
		sleep(delay)

	def __init__(self):
		self.finished = True
		self.deck = Deck(52)
		self.player = Player("Johnny")
		self.dealer = ComputerPlayer("Computer Dealer")
		print("Game Created")

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
		print("Deck Shuffle")
		self.deck.shuffle()

	def hit(self, player):
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
		#if (gamepot == 0):
		#	raise Exception('No Money Left')

		Game.log(f"Starting Hand. Player Bets ${player_bet} Dealer Bets ${dealer_bet}. Game Pot at ${gamepot} ")

		self.display_hands()

		player_score = self.players_turn()
		if (player_score > 21):
			Game.log("**** PLAYER BUST **** DEALER WINS")
			dealer.winbet(gamepot)

		else:
			dealer_score = self.dealers_turn(player_score)
			if (dealer_score > 21):
				player.winbet(gamepot)
				Game.log("**** DEALER BUST **** PLAYER WINS")
			elif (dealer_score > player_score):
				dealer.winbet(gamepot)
				Game.log(f"DEALER WINS DEALER: {dealer_score} PLAYER:{player_score}")

			else:
				player.winbet(gamepot)
				Game.log(f"PLAYER WINS PLAYER:{player_score} DEALER: {dealer_score}")


		# Game Finished Reveal all cards
		self.display_hands(True)
		Game.log(f"PLAYER'S POT: ${player.wallet} DEALER'S POT: ${dealer.wallet}")
		#self.players_go(player,self.calc_score(computer))
		#self.dealers_go(computer,self.calc_score(player))
		#wallet_product = player.wallet * dealer.wallet
		#Game.log(f" Wallets {wallet_product}")

		if (player.wallet * dealer.wallet < 0.01):
			raise Exception('No Money Left')

		return True


	def dealers_turn(self, target_score):

		player = self.player
		dealer = self.dealer

		self.display_hands(True)
		score = self.calc_score(dealer)

		Game.log(f"DEALERS TURN Target Score:{target_score} Current Score: {score}")

		while (score < target_score and score <= Game.HOUSERULES):
			#dealt_card =
			self.prompt_input("Dealer to Hit - Press return to continue", str, [''])
			sleep(1)
			self.hit(dealer)
			dealt_card = dealer.last_card()
			score = self.calc_score(dealer)

			Game.log(f"***DEALER HITS*** Card {Card.describe(dealt_card)} current score {score}")
			self.display_hands(True)
			sleep(3)

		Game.log(f"***DEALER FINISHES*** Score of {score}")
		return score

	def prompt_input(self, msg, inputType = str, allowedSet=None):
	    #print(allowedSet,type(allowedSet)
		while (True):
			try:
				res = inputType(input(f"{msg} {allowedSet}"))
				if (allowedSet is not None and res not in allowedSet):
					raise Exception('Not in allowed Set')
				break
			except ValueError as e1:
				print(f"1:Some Error {e1}")
			except Exception as e2:
				print(f"2:Some Error {e2}")
			finally:
				pass

		return res

	def players_turn(self):
		deck = self.deck
		player = self.player
		dealer = self.dealer
		while True:
			response = self.prompt_input("Hit or Stick?",str,['h','s'])
			if (response == 's'):
				return self.calc_score(player)
			else:
				self.hit(player)
				score = self.calc_score(player)
				print(f"Hit score {score} {deck}")
				self.display_hands()
				sleep(1)
				if (score > 21):
					return score



	def display_hands(self, reveal_all = False):
		player = self.player
		dealer = self.dealer

		player_hand_details = self.build_card_display(player)
		dealer_hand_details = self.build_card_display(dealer)

		self.display("Player", player_hand_details, self.calc_score(player))
		self.display(f"Dealer reveal all={reveal_all}", dealer_hand_details, self.calc_score(dealer), reveal_all)
#		self.display(f"Actual Dealer Cards (Debug)", dealer_hand_details, self.calc_score(dealer), True)

	def display_deck(self):
		deck = self.deck
		deck_details = BlackJackCard.build_card_details(deck.get_cards())
		print(f"Deck {deck}")

#({'suit': 'Hearts', 'values': 5, 'rank': 'Five'}, {'suit': 'Diamonds', 'values': 11, 'rank': 'Ace'}, {'suit': 'Hearts', 'values': 8, 'rank': 'Eight'})

	def display(self,title, details, actual_score, reveal_all = True):
		revealed_hand = details['hand'] if reveal_all else details['hand'][:-1]
		revealed_score = actual_score if reveal_all else sum([item['values'] for item in revealed_hand])
		rhand_str = "\n".join([f"{item['rank']} of {item['suit']}" for item in revealed_hand])
		print(f"***{title} Cards***\n{rhand_str}\nrevealed score : {revealed_score}, actual Score {actual_score}")
#		print(f"{details}")

	def calc_score(self, player):
		playerhand = player.hand
		return BlackJackCard.calc_score(playerhand.cards)

	def build_card_display(self,player):
		playerhand = player.hand
		return {'score': self.calc_score(player), 'hand' : BlackJackCard.build_card_details(playerhand.cards)}



	def __str__(self):
		return f"Game : {self.player},\n{self.dealer},\n{self.deck}"
