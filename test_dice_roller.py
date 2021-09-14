"""Unit tests for dice_roller.py"""
import unittest


class DiceRollerTests(unittest.TestCase):
    # create an instance of dice_roller
    # test <dice_roller.roll()> fails due to no input
    # test <dice_roller.roll((1, 20))> returns {min: 1, max: 20, median: 10.5}
    # test <dice_roller.roll((1, 20), (2, 10))> returns {min: 3, max: 40, median: 21.5}
    # test <dice_roller.roll((1, 20), (2, 10), (1, 100))> returns {min: 4, max: 140, median: 72}
    # test <dice_roller.roll([1, 20], [2, 10], [1, 100])> returns {min: 4, max: 140, median: 72}
    # test <dice_roller.roll((10, 2))> returns {min: 10, max: 20, median: 15}
    # test <dice_roller.roll((10, 1))> returns {min: 10, max: 10, median: 10}
    # test <dice_roller.roll((0, 5))> returns {min: 0, max: 0, median: 0}
    # test <dice_roller.roll((10, 0))> returns {min: 0, max: 0, median: 0}
    # test <dice_roller.roll((1, -10))> fails due to negative sided die
    # test <dice_roller.roll((-1, 10))> fails due to negative number of dice
    # test <dice_roller.roll({2, 5})> fails due to no input not being a list or tuple
    pass