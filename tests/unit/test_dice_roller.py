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

    def test_3_rolls(self):
        roll_1 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        self.assertIn(roll_1[0], range(4, 140+1))
        self.assertEqual(roll_1[1:], (4, 140, 72))

    # test <dice_roller_instance.roll((1, 20), (2, 10), (1, 100))> returns (<any int from 4 to 140> 4, 140, 72)
    # test <dice_roller_instance.roll([1, 20], [2, 10], [1, 100])> returns (<any int from 4 to 140> 4, 140, 72)
    # test <dice_roller_instance.roll((10, 1))> returns (10, 10, 10, 10)
    # test <dice_roller_instance.roll((0, 5))> returns (0, 0, 0, 0)
    # test <dice_roller_instance.roll((10, 0))> returns (0, 0, 0, 0)
    # test <dice_roller_instance.roll((1, -10))> fails due to negative sided die
    # test <dice_roller_instance.roll((-1, 10))> fails due to negative number of dice
    # test <dice_roller_instance.roll({2, 5})> fails due to no input not being a list or tuple
    # test <dice_roller_instance.roll('egg')> fails due to no input not being a list or tuple

    pass