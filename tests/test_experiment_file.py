import unittest
import os


class ExperimentingTest(unittest.TestCase):
    def test_experiment_method(self):
        your_path = os.getcwd()
        acceptable_roles = {"README.md": 1, "test_experiment_file.py": 9}
        found_roles = {}

        for root, dirs, files in os.walk(your_path, topdown=True):

            dirs[:] = [d for d in dirs if d not in ['.git', '.idea', 'personal_notes', '__pycache__', '.pytest_cache',
                                                    '.github']]

            for file in files:
                print(f"Dealing with file {os.path.join(root, file)}")
                with open(os.path.join(root, file), "r") as f:
                    file_string = f.read()
                    num_roles = file_string.count('role')
                    if num_roles > 0:
                        found_roles[file] = num_roles

        self.assertEqual(found_roles, acceptable_roles)

if __name__ == "__main__":
    unittest.main()
