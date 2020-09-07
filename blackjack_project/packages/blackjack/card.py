class Card():

	RANKS = ('Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
	SUIT = ('Clubs', 'Spades', 'Hearts', 'Diamonds')

	@staticmethod
	def get_card_id(rank, suit):
		return Card.RANKS.index(rank) + 13*Card.SUIT.index(suit)

	@staticmethod
	def describe(id):
		return f"{Card.RANKS[id % 13]} of {Card.SUIT[int(id / 13)]}"

	def __init__(self):
		self.id = id
		self.suit = Card.SUIT[int(id / 13)]
		self.rank = Card.RANKS[id % 13]

	@property
	def text(self):
		return f"{self.rank} of {self.suit}"

	def __str__(self):
		return f"Card id: {self.id} Name: {self.rank} of {self.suit}"
