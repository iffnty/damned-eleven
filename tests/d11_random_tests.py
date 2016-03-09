import unittest
from d11_random import deal_cards, play_card, open_cards, determine_winner


class ActualDealingTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = set(range(1,11)) ^ {"J"}
        self.player_hand, self.house_hand, self.last_card = deal_cards(self.deck)


class DealCardsTests(ActualDealingTestCase):
    def test_equal_hand_size(self):
        self.assertTrue(len(self.player_hand) == len(self.house_hand), 'Hands size differ')

    def test_player_dealt_from_deck(self):
        self.assertEqual(self.player_hand, self.player_hand & self.deck)

    def test_house_dealt_from_deck(self):
        self.assertEqual(self.house_hand, self.house_hand & self.deck)

    def test_last_card_dealt_from_deck(self):
        self.assertTrue(self.last_card in self.deck)

    def test_no_identical_cards(self):
        self.assertEqual(set(), self.player_hand & self.house_hand)

    def test_last_card_is_not_in_player_deck(self):
        self.assertFalse(self.last_card in self.player_hand)

    def test_last_card_is_not_in_house_deck(self):
        self.assertFalse(self.last_card in self.house_hand)


class PlayCardTests(ActualDealingTestCase):
    def test_decrease_number_of_cards_in_hands(self):
        player_hand_before_play, house_hand_before_play = self.player_hand.copy(), self.house_hand.copy()
        play_card(self.player_hand, self.house_hand)
        self.assertEqual(len(player_hand_before_play) - 1, len(self.player_hand), 'Player hand size has not changed')
        self.assertEqual(len(house_hand_before_play) - 1, len(self.house_hand), 'House hand size has not changed')

    def test_played_cards_are_removed_from_hands(self):
        player_card, house_card = play_card(self.player_hand, self.house_hand)
        self.assertFalse(player_card in self.player_hand, 'Played card has not been removed from player\'s hand')
        self.assertFalse(house_card in self.house_hand, 'Played card has not been removed from house\'s hand')


class OpenCardsTests(unittest.TestCase):
    def test_player_wins_number_cards(self):
        self.assertEqual("Player", open_cards(8, 2))

    def test_house_wins_number_cards(self):
        self.assertEqual("House", open_cards(1, 10))

    def test_player_wins_joker_vs_number(self):
        self.assertEqual("Player", open_cards("J", 10))

    def test_house_wins_joker_vs_number(self):
        self.assertEqual("House", open_cards(8, "J"))

    def test_player_loses_joker_vs_one(self):
        self.assertEqual("House", open_cards("J", 1))

    def test_house_loses_joker_vs_one(self):
        self.assertEqual("Player", open_cards(1, "J"))


class DetermineWinnerTests(unittest.TestCase):
    def test_player_scores_three_last_card_joker(self):
        outcome = determine_winner(3, 2, "J")
        self.assertEqual("Player", outcome.winner)
        self.assertFalse(outcome.win_by_joker)

    def test_player_scores_three_last_card_numeric(self):
        outcome = determine_winner(3, 2, 5)
        self.assertEqual("Player", outcome.winner)
        self.assertFalse(outcome.win_by_joker)

    def test_house_scores_three_last_card_joker(self):
        outcome = determine_winner(1, 3, "J")
        self.assertEqual("Player", outcome.winner)
        self.assertTrue(outcome.win_by_joker)

    def test_house_scores_three_last_card_numeric(self):
        outcome = determine_winner(2, 3, 10)
        self.assertEqual("House", outcome.winner)
        self.assertFalse(outcome.win_by_joker)


if __name__ == '__main__':
    unittest.main()
