import os
import json


class WordNotFound(Exception):
    def __init__(self, word):
        self.fail = f"*{word}* was not found in this database"
    
    def __str__(self):
        return self.fail

class GrabJsonData:
    def __init__(self, filename: str):
        with open(f'{filename}') as f:
            self.data = json.load(f)
    
    def __dict__(self):
        return dict(self.data)    
    
    def __len__(self):
        return len(self.data)   

class StripPath:
    "Strips the path from a filename"
    def __init__(self, filename: str):
        self.path = os.path.basename(filename)

    def __len__(self):
        return len(self.path)

    def __str__(self):
        return self.path