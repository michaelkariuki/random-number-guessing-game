import unittest
from unittest.mock import patch, call
from Guessing import MiniGame

class TestMiniGame(unittest.TestCase):

    def test_initialization(self):
        game = MiniGame()
        self.assertEqual(game.range_limit, 30)
        self.assertTrue(1 <= game.random_num <= 31)
        self.assertEqual(game.points, 10)
        self.assertEqual(game.guess_range_threshold, 10)
        self.assertEqual(game.guess_list, [])

    def test_guess_state_warm(self):
        game = MiniGame()
        game.random_num = 10
        self.assertEqual(game.guess_state(12), "Hint : You are warm!")

    def test_guess_state_cold(self):
        game = MiniGame()
        game.random_num = 10
        self.assertEqual(game.guess_state(21), "Hint : You are cold!")

    def test_parse_guess_correct_guess(self):
        game = MiniGame()
        game.random_num = 15
        self.assertEqual(game.parse_guess(15), 1)

    def test_parse_guess_incorrect_guess(self):
        game = MiniGame()
        game.random_num = 15
        self.assertEqual(game.parse_guess(10), 0)

    def test_give_factor(self):
        game = MiniGame()
        game.random_num = 12
        factor = game.give_factor(2)
        self.assertTrue(factor.startswith("Hint : Number is a factor of"))

    def test_get_guess_range(self):
        game = MiniGame()
        game.random_num = 20
        self.assertEqual(game.get_guess_range(15), 5)


    @patch('sys.exit')
    @patch('builtins.print')
    def test_parse_game_state_win(self, mock_print, mock_exit):
        game = MiniGame()
        game.parse_game_state(1)

       # expected calls to print
        expected_calls = [
            call(f'You Won!!! Number to guess : {game.random_num} Guesses : []'),
            call('Game has closed.')
        ]
        # Assert the expected calls to print
        mock_print.assert_has_calls(expected_calls)

        # Assert that sys.exit was called
        mock_exit.assert_called_once_with()
    
    
    @patch('sys.exit')
    @patch('builtins.print')
    def test_parse_game_state_loss(self, mock_print, mock_exit):
        game = MiniGame()
        game.points = 1
        self.assertEqual(game.parse_game_state(0), None)
        
        # expected calls to print
        expected_calls = [
            call(f"You lost!!! Number to guess : {game.random_num} Guesses : {game.guess_list}"),
            call('Game has closed.')
        ]

        # Assert the expected calls to print
        mock_print.assert_has_calls(expected_calls)

        # Assert that sys.exit was called
        mock_exit.assert_called_once_with()

    def test_parse_game_state_invalid_state(self):
        game = MiniGame()
        with self.assertRaises(AssertionError):
            game.parse_game_state("invalid_state")

if __name__ == '__main__':
    unittest.main()
