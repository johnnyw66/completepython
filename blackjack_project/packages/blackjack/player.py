from packages.blackjack.hand import Hand
from packages.blackjack.prompt import Prompt
from packages.blackjack.blackjackcard import BlackJackCard


class Player():
    """
    """

    def __init__(self,name):
        self.name = name
        self.hand = Hand(f"{name}'s Hand'")
        self.wins = 0
        self.bets = 0
        self.wallet = 100

    def add(self, cards):
        self.hand.add(cards)

    def get_hand(self):
        return self.hand.cards

    def retrieve_cards(self):
        return self.hand.retrieve_cards()

    def last_card(self):
        return self.get_hand()[-1]

    def placebet(self, amount):
        bet = min(self.wallet, amount)
        self.wallet -= bet
        self.bets += 1
        return bet

    def winbet(self, amount):
        self.wallet += amount
        self.wins += 1


    def players_turn(self, deck, opponent_cards, calc_score_fn, display_fn):
            raise Exception('This is an Abstract Function')


    def __str__(self):

        perc = 0 if (self.bets == 0) else 100*self.wins / self.bets
        return f"Player: {self.name}, {self.hand}, Wallet: {self.wallet} Bets: {self.bets} Wins: {self.wins}  Percentage: {perc}"


class HumanPlayer(Player):

    def turn(self, deck, opponent, calc_score_fn, display_fn):
        while True:
            response = Prompt.prompt("Hit or Stick?",str,['h','s'])
            if (response == 's'):
                return calc_score_fn(self)
            else:
                # hit
                dealt = deck.deal(1)
                self.add(dealt)

                score = calc_score_fn(self)
                display_fn()
                if (score > 21):
                    return score


class ComputerPlayer(Player):

    def turn(self, deck, opponent, calc_score_fn, display_fn):
        while True:
            current_score = calc_score_fn(self)
            if (current_score > 16):
                return current_score
            else:
                # hit
                dealt = deck.deal(1)
                self.add(dealt)

                display_fn()
                score = calc_score_fn(self)
                if (score > 21):
                    return score


class Dealer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.wallet = 1000000 #10000000



    def turn(self, deck, opponent, calc_score_fn, display_fn):

        target_score = calc_score_fn(opponent)

        score = calc_score_fn(self)

        while (score < target_score and score <= BlackJackCard.HOUSERULES):
            #Prompt.prompt("Dealer to Hit - Press return to continue", str, [''])
            #sleep(3)

            # hit
            dealt = deck.deal(1)
            self.add(dealt)
        	#Game.log(f"***DEALER HITS*** Card {Card.describe(dealt_card)} current score {score}")
            display_fn(True)
            score = calc_score_fn(self)

        return score
