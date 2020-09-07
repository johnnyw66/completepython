from packages.blackjack.hand import Hand

class Player():
    """
    """

    def __init__(self,name):
        self.name = name
        self.hand = Hand(f"{name}'s Hand'")
        self.wallet = 100

    def add(self, cards):
        self.hand.add(cards)

    def get_hand(self):
        return self.hand.cards

    def retrieve_cards(self):
        return self.hand.retrieve_cards()
        
    def last_card(self):
        return self.get_hand()[-1]

    def __str__(self):
        return f"Player: {self.name}, {self.hand}, Wallet: {self.wallet}"

    def placebet(self, amount):
        bet = min(self.wallet, amount)
        self.wallet -= bet
        return bet

    def winbet(self, amount):
        self.wallet += amount


class ComputerPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.wallet = 10000000
