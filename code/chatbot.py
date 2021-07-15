# # library
import os

# for train
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

# for push intense.json to the github
import subprocess

# # our module
from training import update_intense
from logger import Logger


def check_dir(name, our_path=os.path.dirname(os.path.abspath(__file__))) -> str:
    """
    :param name: dir name
    :param our_path: path to our dir
    :return: path to the created directory
    """

    arr = os.listdir(path='.')
    return_path = '{}/{}'.format(our_path, name)
    if name not in arr:
        os.mkdir(return_path)

    return return_path


class ChatBot(object):

    def __init__(self):
        update_intense()

        self.lemmatizer = WordNetLemmatizer()
        self.full_intents = json.loads(open('src/intense.json').read())

        self.languages = [language for language in self.full_intents.keys()]
        self.language = 'en'

        tmp_path = check_dir('src')
        self.intents = self.full_intents['en']
        self.words = pickle.load(open(f'{tmp_path}/words_{self.language}.pkl', 'rb'))
        self.classes = pickle.load(open(f'{tmp_path}/classes_{self.language}.pkl', 'rb'))
        self.model = load_model(f'{tmp_path}/chatbotmodel_{self.language}.h5')

    def get_languages(self) -> str:
        """
        :return: get string with our languages. Example: 'en, ru'
        """

        message = ''
        for language in self.languages:
            message += f'{language}, '
        message = message[:-2]
        return message

    def get_training(self) -> list:
        """
        :return: list with elements intense.json
        """

        result = []
        languages = self.full_intents.keys()
        for i, language in enumerate(languages):
            if i == 0:
                result.append(f'{language}:\n')
            else:
                result.append(f'\n{language}:\n')
            elements = self.full_intents[language]['intents']
            for element in elements:
                mes = f"tag: {element['tag']}\npatterns: "
                for pattern in element['patterns']:
                    mes += f"\"{pattern}\", "
                mes = f'{mes[:-2]}\nresponse: '
                for response in element['responses']:
                    mes += f"\"{response}\", "
                mes = f'{mes[:-2]}\n'
                result.append(mes)

        return result

    def add_training(self, message: str) -> str:
        """
        :param message: string like <language> : <tag> : <pat or res (pat - pattern, res - response)> : <text>
        :return: response
        """

        try:
            if message.find(':') == -1:
                return 'Missed \':\''
            language = message[:message.find(':')]
            tmp = message[message.find(':') + 1:]

            if tmp.find(':') == -1:
                return 'Missed \':\''
            tag = tmp[:tmp.find(':')]
            tmp = tmp[tmp.find(':') + 1:]

            if tmp.find(':') == -1:
                return 'Missed \':\''
            param = tmp[:tmp.find(':')]

            text = tmp[tmp.find(':') + 1:]
        except:
            return 'Incorrect syntax'

        if not(param in ['pat', 'res']):
            return f'{param} (3 element) isn\'t pat or res'
        if param == 'pat':
            param = 'patterns'
        else:
            param = 'responses'

        # if there is no way to language
        try:
            self.full_intents[language]
        except KeyError:
            self.full_intents[language] = {'intents': []}

        # check if there is such a tag
        saved = False
        for elem in self.full_intents[language]['intents']:
            if elem['tag'] == tag:
                saved = True
                if param == 'patterns':
                    text = text.lower()
                elem[param].append(text)
        # if he is not there
        if not saved:
            if param == 'patterns':
                text = text.lower()
                self.full_intents[language]['intents'].append({'tag': tag, 'patterns': [text], 'responses': []})
            else:
                self.full_intents[language]['intents'].append({'tag': tag, 'patterns': [], 'responses': [text]})

        # save in json file
        with open('src/intense.json', 'w') as file:
            json.dump(self.full_intents, file, indent=2, ensure_ascii=False)

        return 'Done!'

    def training(self) -> str:
        """
        start training
        """

        try:
            update_intense()
            return 'Done!'
        except Exception as e:
            logger = Logger('training')
            logger.error()
            return logger.warning()

    def change_language(self, language) -> str:
        """
        change the communication language of the whole bot
        :param language: language we need
        :return: string with result
        """

        if language == self.language:
            return 'This language already stands'
        if not (language in self.languages):
            return 'The bot does not support such a language'

        self.language = language

        tmp_path = check_dir('src')
        self.intents = self.full_intents[self.language]
        self.words = pickle.load(open(f'{tmp_path}/words_{self.language}.pkl', 'rb'))
        self.classes = pickle.load(open(f'{tmp_path}/classes_{self.language}.pkl', 'rb'))
        self.model = load_model(f'{tmp_path}/chatbotmodel_{self.language}.h5')

        return 'Language set!'

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]

        return sentence_words

    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for word_s in sentence_words:
            for i, word in enumerate(self.words):
                if word == word_s:
                    bag[i] = 1

        return np.array(bag)

    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        error_threshold = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > error_threshold]

        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})

        return return_list

    def get_response(self, intents_list, intents_json):
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        try:
            return result
        except UnboundLocalError:
            return 'I didn\'t understand your message('
