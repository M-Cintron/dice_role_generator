"""Unit tests for dice_roller.py"""
import unittest

# Note: the roll method returns a tuple; (roll result, min possible roll, max possible roll, median roll)
# Todo: How would I go about testing the return value of something random?
# Todo: Change all 'dice_roller's with the name of the instance of dice_roller
# Maybe have dice_roller.roll() roll (1, 20) as default?
class DiceRollerTests(unittest.TestCase):
    # create an instance of dice_roller
    # test <dice_roller.history()> returns {}
    # test <dice_roller.roll()> returns (<any int from 1 to 20>, 1, 20, 10.5)
    # test <dice_roller.roll((1, 20), (2, 10), (1, 100))> returns (<any int from 4 to 140> 4, 140, 72)
    # test <dice_roller.roll([1, 20], [2, 10], [1, 100])> returns (<any int from 4 to 140> 4, 140, 72)
    # test <dice_roller.roll((10, 1))> returns (10, 10, 10, 10)
    # test <dice_roller.roll((0, 5))> returns (0, 0, 0, 0)
    # test <dice_roller.roll((10, 0))> returns (0, 0, 0, 0)
    # test <dice_roller.roll((1, -10))> fails due to negative sided die
    # test <dice_roller.roll((-1, 10))> fails due to negative number of dice
    # test <dice_roller.roll({2, 5})> fails due to no input not being a list or tuple
    # test <dice_roller.roll('egg')> fails due to no input not being a list or tuple
    # test <dice_roller.history()> returns {'Roll_0': {'Dice': ((1, 20)), 'Result': '<any int from 1 to 20>', 'Min': 1,
    # 'Max': 20, 'Median': 10.5}, 'Roll_1': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': '<any int from 4 to 140>', 'Min': 4,
    # 'Max': 140, 'Median': 72}, 'Roll_2': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': '<any int from 4 to 140>', 'Min': 4,
    # 'Max': 140, 'Median': 72}, 'Roll_3': {'Dice': ((10, 1)), 'Result': 10, 'Min': 10,
    # 'Max': 10, 'Median': 10}, 'Roll_4': {'Dice': ((0, 5)), 'Result': 0, 'Min': 0,
    # 'Max': 0, 'Median': 0}, 'Roll_5': {'Dice': ((10, 0)), 'Result': 0, 'Min': 0,
    # 'Max': 0, 'Median': 0}}
    # run <dice_roller.clear()>
    # test <dice_roller.history()> returns {}
    pass