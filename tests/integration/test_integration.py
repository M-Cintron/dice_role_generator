"""Integration tests for dice_roller.py"""
import unittest
import dice_roller


class DiceRollerIntegrationTests(unittest.TestCase):

    # test that .history() returns {} when no rolls have been made
    def test_no_history(self):
        dice_roller_instance = dice_roller.DiceRoller()
        self.assertEqual(dice_roller_instance.history(), {})

    # test .history() returns the correct output after running .roll()
    def test_history(self):
        dice_roller_instance = dice_roller.DiceRoller()

        # run 4 rolls, save the results so we can get the role result for the assert below
        result_0 = dice_roller_instance.roll((1, 20))
        result_1 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_2 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_3 = dice_roller_instance.roll((10, 1))

        self.assertEqual(dice_roller_instance.history(),
                         {
                             'Roll_0': {'Dice': ((1, 20),), 'Result': result_0[0], 'Min': 1, 'Max': 20, 'Median': 10.5},
                             'Roll_1': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': result_1[0], 'Min': 4,
                                        'Max': 140, 'Median': 72.0},
                             'Roll_2': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': result_2[0], 'Min': 4,
                                        'Max': 140, 'Median': 72.0},
                             'Roll_3': {'Dice': ((10, 1),), 'Result': result_3[0], 'Min': 10, 'Max': 10, 'Median': 10.0}
                         }
                         )

    # test that .history() is not messed up by invalid rolls
    def test_history_with_invalid_inputs(self):
        dice_roller_instance = dice_roller.DiceRoller()
        result_0 = dice_roller_instance.roll((1, 15))
        result_1 = dice_roller_instance.roll((1, 30), (2, 10), (1, 100))
        try:
            dice_roller_instance.roll((0, 5))
        except ValueError:
            pass
        try:
            dice_roller_instance.roll((10, 0))
        except ValueError:
            pass
        result_2 = dice_roller_instance.roll((1, 20), (2, 10))
        result_3 = dice_roller_instance.roll((5, 4))
        result_4 = dice_roller_instance.roll()

        self.assertEqual(dice_roller_instance.history(),
                         {
                             'Roll_0': {'Dice': ((1, 15),), 'Result': result_0[0], 'Min': 1, 'Max': 15, 'Median': 8.0},
                             'Roll_1': {'Dice': ((1, 30), (2, 10), (1, 100)), 'Result': result_1[0], 'Min': 4,
                                        'Max': 150, 'Median': 77.0},
                             'Roll_2': {'Dice': ((1, 20), (2, 10)), 'Result': result_2[0], 'Min': 3,
                                        'Max': 40, 'Median': 21.5},
                             'Roll_3': {'Dice': ((5, 4),), 'Result': result_3[0], 'Min': 5, 'Max': 20, 'Median': 12.5},
                             'Roll_4': {'Dice': ((1, 20),), 'Result': result_4[0], 'Min': 1, 'Max': 20, 'Median': 10.5},
                         }
                         )

    # test that .clear() empties the instance's record and that .history() returns {}
    def test_clear_history(self):
        dice_roller_instance = dice_roller.DiceRoller()
        dice_roller_instance.roll((1, 200))
        dice_roller_instance.roll((2, 20), (2, 13), (1, 100))
        dice_roller_instance.roll((1, 20), (2, 6), (1, 10))
        dice_roller_instance.roll((10, 2))

        dice_roller_instance.clear()

        self.assertEqual(dice_roller_instance.history(), {})
