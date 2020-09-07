from random import shuffle

class Deck():
    """
    """

    def __init__(self, size = 52):
        self.cards = [id for id in range(0,size)]

    def shuffle(self):
        shuffle(self.cards)

    # Returns an array of card
    def deal(self, amount=1):
        dealt = self.cards[:amount]
        self.cards = self.cards[amount:]
        return dealt

    def return_cards(self, cards):
        self.cards.extend(cards)

    def get_cards(self):
        return tuple(self.cards)

    def __str__(self):
        return f"Card Deck: {self.cards}(size={len(self.cards)})"
