import unittest
import dice_roller


class DiceRollerIntegrationTests(unittest.TestCase):
    def test_no_history(self):
        dice_roller_instance = dice_roller.DiceRoller()
        self.assertEqual(dice_roller_instance.history(), {})

    def test_history(self):
        dice_roller_instance = dice_roller.DiceRoller()

        # run 4 rolls, save the results so we can get the role result for the assert below
        result_0 = dice_roller_instance.roll((1, 20))
        result_1 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_2 = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        result_3 = dice_roller_instance.roll((10, 1))

        self.assertEqual(dice_roller_instance.history(),
                         {
                             'Roll_0': {'Dice': ((1, 20)), 'Result': result_0[0], 'Min': 1, 'Max': 20, 'Median': 10.5},
                             'Roll_1': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': result_1[0], 'Min': 4,
                                        'Max': 140, 'Median': 72},
                             'Roll_2': {'Dice': ((1, 20), (2, 10), (1, 100)), 'Result': result_2[0], 'Min': 4,
                                        'Max': 140, 'Median': 72},
                             'Roll_3': {'Dice': ((10, 1)), 'Result': result_3[0], 'Min': 10, 'Max': 10, 'Median': 10}
                         }
                         )

    def test_history_with_invalid_inputs(self):
        dice_roller_instance = dice_roller.DiceRoller()
        try:
            dice_roller_instance.roll((0, 5))
        except ValueError:
            pass
        try:
            dice_roller_instance.roll((10, 0))
        except ValueError:
            pass

# clear()> then test <dice_roller_instance.history()> returns {}
