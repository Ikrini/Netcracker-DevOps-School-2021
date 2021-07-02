# # library
import unittest
import os

# # modules
from config import path_to_dir


class TestForJenkins(unittest.TestCase):

    def test_existence_of_files(self):
        paths = ('src/intense.json', 'main.py', 'bot.py', 'chatbot.py', 'config.py', 'logger.py', 'training.py')

        for name in paths:
            path = f'{path_to_dir}/{name}'
            exist = os.path.exists(path)
            if not exist:
                print(f'FILE NOT EXIST: {name} ({path})')
            self.assertTrue(exist)


if __name__ == "__main__":
    unittest.main()
