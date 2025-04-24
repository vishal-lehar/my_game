import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    
    # Helper functions.
    def roll_many(self, n, pins):
        for _ in range(n):
            self.game.roll(pins)
    
    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
    
    def roll_strike(self):
        self.game.roll(10)
        
    # Test cases...
    def test_gutter_game(self):
        print("Test for a gutter game (20 times 0 pin)")
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())
    
    def test_all_ones(self):
        print("Test for all ones (20 times 1 pin)")
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())
    
    def test_one_spare(self):
        print("Test for a spare followed by a 3")
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.game.score())
    
    def test_one_strike(self):
        print("Test for a strike followed by a 3 and a 4")
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.game.score())
    
    def test_perfect_game(self):
        print("Test for a perfect game (12 times 10)")
        self.roll_many(12, 10)
        self.assertEqual(300, self.game.score())
    
    def test_incomplete_game(self):
        print("Test that an error is raised for an incomplete game")
        self.roll_many(11, 10)
        with self.assertRaises(ValueError):
            self.game.score()
    
    def test_invalid_pins(self):
        print("Test that an error is raised for invalid number of pins")
        with self.assertRaises(ValueError):
            self.game.roll(11)
        
        with self.assertRaises(ValueError):
            self.game.roll(-1)
            
    def test_example_score_card(self):
        print(f"Test sample score card given in the problem.")
        rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
        for roll in rolls:
            self.game.roll(roll)
        self.assertEqual(self.game.score(), 133)
    
if __name__ == "__main__":
    unittest.main()