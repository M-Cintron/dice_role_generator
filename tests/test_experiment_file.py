import unittest
import os


class ExperimentingTest(unittest.TestCase):
    def test_experiment_method(self):
        yourpath = os.getcwd()

        for root, dirs, files in os.walk(yourpath, topdown=True):

            dirs[:] = [d for d in dirs if d not in ['.git', '.idea', 'personal_notes', '__pycache__', '.pytest_cache',
                                                    '.github']]

            for file in files:
                print(f"Dealing with file {os.path.join(root, file)}")
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        print(line)
        self.assertEqual('egg', 'egg')

if __name__ == "__main__":
    unittest.main()
    # for name in dirs:
    #     print('for name in dirs:', os.path.join(root, name))