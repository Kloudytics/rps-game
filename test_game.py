# test_game.py

import unittest
from game import play_round


class TestGame(unittest.TestCase):

    def test_play_round_tie(self):
        result = play_round("rock", "rock")
        self.assertEqual(result, "It's a tie!")

    def test_play_round_user_wins(self):
        result = play_round("rock", "scissors")
        self.assertEqual(result, "You win!")

    def test_play_round_computer_wins(self):
        result = play_round("rock", "paper")
        self.assertEqual(result, "You lose!")


if __name__ == '__main__':
    unittest.main()
