from packages.blackjack.card import Card

class BlackJackCard(Card):

    VALUES = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    @staticmethod
    def get_card_details(id):
        return {'suit' : Card.SUIT[int(id / 13)], 'values' : BlackJackCard.VALUES[id % 13], 'rank':  Card.RANKS[id % 13]}

    @staticmethod
    def build_hand_scores(card_id_array):
        values = [BlackJackCard.VALUES[id % 13] for id in card_id_array]
        return tuple(values)

    @staticmethod
    def build_card_details(card_id_array):
        values = [BlackJackCard.get_card_details(id) for id in card_id_array]
        return tuple(values)

#    @staticmethod
#    def calc_best_score(card_id_array):
#        # Get Valuesfrom card_id_array
#        # and work out nearest score to 21
#        values = BlackJackCard.build_hand_scores(card_id_array)
#
#        return 0

    @staticmethod
    def calc_score(card_id_array):
        # Get Valuesfrom card_id_array
        # and work out nearest score to 21
        values = BlackJackCard.build_hand_scores(card_id_array)
        total_score = sum(values)
        for v in values:
            if (v == 11):
                if (total_score > 21):
                    total_score -= 10

        return total_score


    def __init__(self, id):
        super().__init__(id)
        self.values = BlackJackCard.VALUES[id % 13]

    def __str__(self):
        return f"BlackJackCard id: {self.id}  {self.rank} of {self.suit} value: {self.values}"
