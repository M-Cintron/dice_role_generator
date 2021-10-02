import unittest
import os


class ExperimentingTest(unittest.TestCase):
    maxDiff = None

    def test_experiment_method(self):
        # get the relative path of the dice_roller main directory by getting the current working directory, and removing
        # the tests directory part.
        path_of_test_directory = os.getcwd()

        path_parts = path_of_test_directory.split('/')
        print(path_parts)
        dice_roller_index = path_parts.index('dice_roller')
        # splicing off the last two sub directories from ..\dice_roller\tests\typo_hunting so we can have the relative
        # path of the whole directory: ..\dice_roller
        project_relative_path = '/'.join(path_parts[:dice_roller_index + 1])

        # make a dic of file names, relative to the dice_roller main directory, and the values being the number of
        # 'roles' found in them.
        # To add a file to acceptable_roles, include the top two directories are:'dice_roller/dice_roller/'
        acceptable_roles = {"dice_roller/dice_roller/README.md": 1,
                            "dice_roller/dice_roller/dice_roller/__init__.py": 1,
                            "dice_roller/dice_roller/tests/unit/test_dice_roller.py": 1,
                            'dice_roller/dice_roller/tests/integration/test_integration.py': 2}
        found_roles = {}

        # go through every file in the main dice_roller directory, including those in sub directories
        for root, dirs, files in os.walk(project_relative_path, topdown=True):
            # change the list of directories to walk through to NOT include the named directories
            dirs[:] = [d for d in dirs if d not in ['.git', '.idea', 'personal_notes', '__pycache__', '.pytest_cache',
                                                    '.github', 'typo_hunting']]

            # go through each file individually
            for file in files:
                with open(os.path.join(root, file), "r") as f:

                    # make the file into one string and make everything lowercase
                    file_string = f.read()
                    file_string = file_string.lower()
                    num_roles = file_string.count('role')

                    # if 'role's are found in a file
                    if num_roles > 0:
                        # get the relative path of the current file starting from the main dice_roller directory
                        file_path_parts = root.split('/')
                        dice_roller_index = file_path_parts.index('dice_roller')
                        relative_file_path = '/'.join(file_path_parts[dice_roller_index:])

                        # add the relative file path and the number of 'roles found to the found_roles dic
                        found_roles[f'{relative_file_path}/{file}'] = num_roles

        self.assertEqual(found_roles, acceptable_roles)
