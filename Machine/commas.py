from collections import Counter
import json
from spellchecker import SpellChecker

class itentify:
    def __init__(self, text: str):
        num = []
        for e, i in enumerate(text):
            if i == ",":
                num.append(e)

        if len(num) > 1:
            coms = []
            for iter, number in enumerate(num):
                if max(num) == num[iter]:
                    if (number-num[iter-1]) <= 15:
                        coms.append(number)
                
                else:
                    number1 = number
                    number2 = num[iter+1]
                    diff = number2-number1
                    if diff <= 15:
                        coms.append(number1)
                        coms.append(number2)
            
            coms_sorted = Counter(coms)
            coms = [k for k, v in coms_sorted.items() if v >= 0]
            
            text_list = list(text)

            for iter, num in enumerate(coms):
                text_list.pop(num-iter)
            
            text = "".join(text_list) 

        self.commas = text

class Determiners:
    def __init__(self, text: list):
        words = ["the", "a", "an", "this", "that", "these", "those"]
        
        for iter, word in enumerate(text):
            if word in words:
                text.pop(iter)
        
        self.text = text
    
    def split_len(word: str, suffix: dict):
        length = len(word)
        variations = {}
        for diction in suffix["intents"]:
            if diction == max(suffix["intents"]):
                try:
                    locate = word.index(diction["tag"])
                    
                    if locate > .5*length:
                        word.replace(suffix["tag"], "")
                        return word
                except ValueError:
                    variations.update(word)
            try:
                locate = word.index(diction["tag"])
                
                if locate > .5*length:
                    word.replace(suffix["tag"], "")
                    return word
            except ValueError:
                variations.update(word)

    def suffix_strip(self):
        with open("Machine\Data\Suffixes.json") as f:
            users = json.load(f)
        
        text = self.text
        word_list = []

        if type(text) is list[list]:
            for sentence in text:
                for word in sentence:
                    word_list.append(Determiners.split_len(word, dict(users)))


class Tokenize:
    def __init__(self, text):
        sent_log = []
        if type(text) is str:
            text.split(" ")
            self.split = text 
        
        elif type(text) is list:
            for sentence in text:
                sent_log.extend(str(sentence).split())
            
            self.split = sent_log
    