"""Unit tests for dice_roller.py"""
import unittest
import dice_roller

# TODO: Should the instance of dice_roller be created inside the test class or here?
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
    def test_str_input(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll('egg')

    # test dice_roller_instance.roll((1.2, 5)) fails due to number of dice not being an int
    def test_float_num_dice(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll((1.2, 5))

    # test dice_roller_instance.roll((3, 1.414)) fails due to the number of sides not being an int
    def test_float_num_sides(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll((3, 1.414))

    # test dice_roller_instance.roll((1,6,2)) fails due to a tuple having more than two values
    def test_excess_values(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll((1, 4, 5))

    # test dice_roller_instance([2]) fails due to a list having only one value
    def test_missing_values(self):
        with self.assertRaises(TypeError):
            dice_roller_instance.roll([2])
