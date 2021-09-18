"""Unit tests for dice_roller.py"""
import unittest
import dice_roller

# Note: the roll method returns a tuple; (roll result, min possible roll, max possible roll, median roll)
# Todo: How would I go about testing the return value of something random?
#     Also, how would I go about testing randomness?

# TODO: the tests involving the history and clear method will have to be changed into integration tests as they
#   involving testing the results of multiple methods working together
dice_roller_instance = dice_roller.DiceRoller()


class DiceRollerTests(unittest.TestCase):

    # test <dice_roller_instance.roll()> returns (<any int from 1 to 20>, 1, 20, 10.5)
    def test_empty_roll(self):
        roll_0 = dice_roller_instance.roll()
        # check that the random number is some number between 1 and 20 (inclusive)
        self.assertIn(roll_0[0], range(1, 20+1))
        # check that the min, max, and median values are correct
        self.assertEqual(roll_0[1:], (1, 20, 10.5))

    # test <dice_roller_instance.roll((1, 20), (2, 10), (1, 100))> returns (<any int from 4 to 140> 4, 140, 72)
    def test_3_rolls(self):
        roll_1 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        self.assertIn(roll_1[0], range(4, 140+1))
        self.assertEqual(roll_1[1:], (4, 140, 72))

    # test <dice_roller_instance.roll([1, 20], [2, 10], [1, 100])> returns (<any int from 4 to 140> 4, 140, 72)
    def test_3_rolls_lists(self):
        roll_2 = dice_roller_instance.roll([1, 20], [2, 10], [1, 100])
        self.assertIn(roll_2[0], range(4, 140+1))
        self.assertEqual(roll_2[1:], (4, 140, 72))

    # test <dice_roller_instance.roll((10, 1))> returns (10, 10, 10, 10)
    def test_10_dice_1_side(self):
        roll_3 = dice_roller_instance.roll((10, 1))
        self.assertEqual(roll_3, (10, 10, 10, 10))

    # test <dice_roller_instance.roll((0, 5))> fails due to rolling 0 dice
    def test_0_dice(self):
        with self.assertRaises(ValueError):
            dice_roller_instance.roll((0, 5))

    # test <dice_roller_instance.roll((10, 0))> fails due to rolling 0 sided dice
    def test_0_sides(self):
        with self.assertRaises(ValueError):
            dice_roller_instance.roll((10, 0))

    # test <dice_roller_instance.roll((1, -10))> fails due to negative sided die
    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            dice_roller_instance.roll((1, -10))

    # test <dice_roller_instance.roll((-1, 10))> fails due to negative number of dice
    def test_negative_dice(self):
        with self.assertRaises(ValueError):
            dice_roller_instance.roll((-1, 10))

    # test <dice_roller_instance.roll({2, 5})> fails due to no input not being a list or tuple
    def test_set_input(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll({2, 5})
    # test <dice_roller_instance.roll('egg')> fails due to no input not being a list or tuple
    # test dice_roller_instance.roll((1.2, 5)) fails due to number of dice not being an int
    # test dice_roller_instance.roll((3, 1.414)) fails due to the number of sides not being an int

    pass