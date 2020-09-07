class Hand():
	DEFAULT_HAND_NAME = 'UNKNOWN'

	@property
	def cards(self):
		return tuple(self._cards)
	#def get_cards(self):
	#	return tuple(self._cards)

	def __init__(self, name=DEFAULT_HAND_NAME):
		self._name = name
		self._cards = []

		
	def retrieve_cards(self):
		cards =  self._cards
		self._cards = []
		return cards

	def empty_hand(self):
		self._cards = []

	def add(self, cards):
		if (type(cards) == list):
			self._cards.extend(cards)
		else:
			self._cards.append(cards)

	def __str__(self):
		return f"Hand: {self._name} Cards holding: {self._cards}(size={len(self._cards)})"
