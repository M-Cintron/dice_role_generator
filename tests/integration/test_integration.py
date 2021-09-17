import unittest
import dice_roller


class DiceRollerIntegrationTests(unittest.TestCase):
    def test_no_history(self):
        dice_roller_instance = dice_roller.DiceRoller()
        self.assertEqual(dice_roller_instance.history(), {})
    # TODO: a dice roller instance will have to roll these dice before the following tests can run
    # test <dice_roller_instance.history()> returns {'Roll_0': {'Dice': ((1, 20)), 'Result': '<any int from 1 to 20>', 'Min': 1,
    # 'Max': 20, 'Median': 10.5}, 'Roll_1': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': '<any int from 4 to 140>', 'Min': 4,
    # 'Max': 140, 'Median': 72}, 'Roll_2': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': '<any int from 4 to 140>', 'Min': 4,
    # 'Max': 140, 'Median': 72}, 'Roll_3': {'Dice': ((10, 1)), 'Result': 10, 'Min': 10,
    # 'Max': 10, 'Median': 10}, 'Roll_4': {'Dice': ((0, 5)), 'Result': 0, 'Min': 0,
    # 'Max': 0, 'Median': 0}, 'Roll_5': {'Dice': ((10, 0)), 'Result': 0, 'Min': 0,
    # 'Max': 0, 'Median': 0}}
    # run <dice_roller_instance.clear()> then test <dice_roller_instance.history()> returns {}