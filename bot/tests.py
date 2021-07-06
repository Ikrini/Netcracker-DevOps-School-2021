# # library
import unittest
import os
import json

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

    def test_structure_intense_json(self):
        with open('src/intense.json', 'r') as file:
            full_intents = json.load(file)

        languages = full_intents.keys()
        for language in languages:
            intense = full_intents[language]
            self.assertTrue('intents' in intense.keys())

            intense = intense['intents']
            for element in intense:
                keys = element.keys()
                headers = ('tag', 'patterns', 'responses')
                for header in headers:
                    self.assertTrue(header in keys)


if __name__ == "__main__":
    unittest.main()
