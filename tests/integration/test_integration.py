"""Integration tests for dice_roller.py"""
import unittest
import dice_roller


class DiceRollerIntegrationTests(unittest.TestCase):

    def test_no_history(self):
        """
        test that .history() returns {} when no rolls have been made
        """
        dice_roller_instance = dice_roller.DiceRoller()
        self.assertEqual(dice_roller_instance.history(), {})

    def test_history(self):
        """
        test .history() returns the correct output after running .roll()
        """
        dice_roller_instance = dice_roller.DiceRoller()

        # run 4 rolls, save the results so we can get the roll result for the assert below
        result_0 = dice_roller_instance.roll((1, 20))
        result_1 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_2 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_3 = dice_roller_instance.roll((10, 1))

        self.assertEqual(
            dice_roller_instance.history(),
            {
                'roll_0': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 20}},
                           'result': result_0[0], 'min': 1, 'max': 20, 'median': 10.5},
                'roll_1': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 20},
                                    'dice_1': {'number_of_dice': 2, 'number_of_sides': 10},
                                    'dice_2': {'number_of_dice': 1, 'number_of_sides': 100}},
                           'result': result_1[0], 'min': 4, 'max': 140, 'median': 72.0},
                'roll_2': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 20},
                                    'dice_1': {'number_of_dice': 2, 'number_of_sides': 10},
                                    'dice_2': {'number_of_dice': 1, 'number_of_sides': 100}},
                           'result': result_2[0], 'min': 4, 'max': 140, 'median': 72.0},
                'roll_3': {'dice': {'dice_0': {'number_of_dice': 10, 'number_of_sides': 1}},
                           'result': result_3[0], 'min': 10, 'max': 10, 'median': 10.0}
            }
        )

    def test_history_with_invalid_inputs(self):
        """
        test that .history() is not messed up by invalid rolls
        """
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
                             'roll_0': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 15}},
                                        'result': result_0[0], 'min': 1, 'max': 15, 'median': 8.0},
                             'roll_1': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 30},
                                                 'dice_1': {'number_of_dice': 2, 'number_of_sides': 10},
                                                 'dice_2': {'number_of_dice': 1, 'number_of_sides': 100}},
                                        'result': result_1[0], 'min': 4, 'max': 150, 'median': 77.0},
                             'roll_2': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 20},
                                                 'dice_1': {'number_of_dice': 2, 'number_of_sides': 10}},
                                        'result': result_2[0], 'min': 3, 'max': 40, 'median': 21.5},
                             'roll_3': {'dice': {'dice_0': {'number_of_dice': 5, 'number_of_sides': 4}},
                                        'result': result_3[0], 'min': 5, 'max': 20, 'median': 12.5},
                             'roll_4': {'dice': {'dice_0': {'number_of_dice': 1, 'number_of_sides': 20}},
                                        'result': result_4[0], 'min': 1, 'max': 20, 'median': 10.5},
                         }
                         )

    def test_clear_history(self):
        """
        test that .clear() empties the instance's record and that .history() returns {}
        """

        dice_roller_instance = dice_roller.DiceRoller()
        dice_roller_instance.roll((1, 200))
        dice_roller_instance.roll((2, 20), (2, 13), (1, 100))
        dice_roller_instance.roll((1, 20), (2, 6), (1, 10))
        dice_roller_instance.roll((10, 2))

        dice_roller_instance.clear()

        self.assertEqual(dice_roller_instance.history(), {})
