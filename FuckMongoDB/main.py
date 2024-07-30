import json   
import os
from tibs.Classes import GrabJsonData, StripPath
from tibs.helpers import Helper


class InvalidFolderPath(Exception):
    def __init__(self, folderPath: str):
        self.message = f"'{folderPath}' does not exist"
    
    def __str__(self):
        return self.message

class MissingParam(Exception):
    def __init__(self, param: str, var: str):
        self.message = f"'{param}' parameter is missing from the variable '{var}'"
    
    def __str__(self):
        return self.message

class JsonPathError(Exception):
    """Makes the JSON usable
    
    Supposed to work in tandam with the Split class"""
    def __init__(self, path: str, filename: str, interval:int):
        try:
            if len(interval) == 0:
                with open(f"{path}\{filename}.json", "w") as f:
                    f.write("{}")
                self.data = f"{path}\{filename}({interval}).json"

            elif len(interval) > 0:        
                with open(f"{path}\{filename}({interval}).json", "w") as f:
                    f.write("{}")
                self.data = f"{path}\{filename}({interval}).json"
        except:
            if interval == None:
                with open(f"{filename}.json", "w") as f:
                    f.write("{}")
                self.data = f"{filename}({interval}).json"

            elif interval >= 0:        
                with open(f"{filename}({interval}).json", "w") as f:
                    f.write("{}")
                self.data = f"{filename}({interval}).json"
    def __str__(self):
        return str(self.data)

def FolderItems(folderPath):
    "Pulls every item from any JSON in a folder"
    dictionary = {}
    
    folder_list = os.listdir(folderPath)

    for file in folder_list:
        with open(f"{folderPath}\{file}") as f:
            data = json.load(f)
            dictionary.update(data)
    return dictionary

def Insert_data(file=None, *args, word:dict, path=""):
    "Locates the word in the database, if it doesn't exist then it will write it in a new file."
    file = Helper.thea_represent(file, args)
        
    try:
        for item in file:
            with open(f"{path}\{item}") as f:
                data = json.load(f)
            
            for key in data:
                if key == list(word):
                    return print(f"Found the word, *{key}* ~ {item}")

    except FileNotFoundError:
        for item in file:
            with open(f"{item}") as f:
                data = json.load(f)
            
            for key in data:
                if key == list(word):
                    return print(f"Found the word, *{key}* ~ {item}")

    Helper.temp_file("temp.json", word)

class DataSpread:
    "This code class deals with the location, and the retriveing, of data"
    @staticmethod
    def locate(filepath: str):
        try:
            dir_list = os.listdir(filepath) 
            return dir_list
        except:
            raise InvalidFolderPath(filepath)
    
    @staticmethod
    def slice(filepath, interval: int, final_notation = ""):
        "Returns the sliced "
        try:
            with open(f"{filepath}") as f:
                data = json.load(f)
            
            interval = interval*500
            interval2 = interval+499

            collection = {}

            if final_notation is True:
                for f, (v,b) in enumerate(dict(data).items()):
                    if f<interval or f>len(data):
                        continue
                    collection[v] = b
            
            else:
                for f, (v, b) in enumerate(dict(data).items()):
                    if f<interval or f>interval2:
                        continue
                    collection[v] = b

            return collection
        
        except FileNotFoundError:
            interval1 = interval*500 
            interval2 = interval1+499

            collection = {}

            for iteration, (v,b) in enumerate(dict(filepath).items()):
                if iteration<interval1 or iteration>interval2:
                    continue
                collection[v] = b
            
            return collection

    @staticmethod
    def log(filename: str, path: str, path2 = ""):
        "Moves JSON files"
        try:
            
            with open(f"{filename}") as f:
                users = json.load(f)
            
            with open(f'{path}\{filename}', 'w') as f:
                json.dump(users, f)
            
        except FileNotFoundError:
            try:
                with open(f"{path}\{filename}") as f:
                    users = json.load(f)

                with open(f"{path}\{filename}", "w") as f:
                    json.dump(users, f)
        
            except FileNotFoundError:
                with open(f"{path2}\{filename}") as f:
                    users = json.load(f)

                with open(f"{path}\{filename}", "w") as f:
                    json.dump(users, f)

class Shard:
    "Class of code that deals with the making, and calculations, of the files"
    @staticmethod
    def count(filename: str): #if its over any number then +1
        try:

            data = len(GrabJsonData(filename))
            rounded = data//500
            if data%500 > 0:
                return rounded+1
            
            return rounded
        
        except:
            data = len(filename)
            rounded = data//500
            if data%500 > 0:
                return rounded+1
            
            return rounded
        
        

    @staticmethod
    def split(filename: str, list_names=False):
        """Input a file and it will split it into smaller, more usable, versions"""
        var = Shard.count(filename)
        length = StripPath(filename)
        ordered_list = []

        for i in range(0, var):
            path = str(JsonPathError(filename[:len(filename)-len(length)], length[:5], i))
            ordered_list.append(path)
            if i == var-1:
                
                with open(f"{path}", "w") as f:
                    json.dump(DataSpread.slice(filename, i, True), f, indent=2)
                continue
            
            with open(f"{path}", "w") as f:
                json.dump(DataSpread.slice(filename, i), f, indent=2)
        
        if list_names is True:
            return ordered_list
            
    def split_dict(data: dict, intervals:int, filename="DataFile"):
        "Input a dictionary and it will shard it into, smaller, more usable items"
        file_list = []
        
        for i in range(0, intervals):
            path = str(JsonPathError(None, filename=filename, interval=i))
            
            file_list.append(path)
            if i == intervals-1:
                with open(f"{path}", "w") as f:
                    json.dump(DataSpread.slice(filepath=data, interval=i), f, indent=2)
                continue

            with open(f"{path}", "w") as f:
                json.dump(DataSpread.slice(filepath=data, interval=i), f, indent=2)

        return file_list
    

def add_keydata(Keyword: dict, folderpath, all_items=False):
    """Input a dictionary, or a json, that you would like appended to a specified folder that holds sharded data.
    
    If all_items is true then every item in the dictionary, that is equal to the keyword variable, will be averaged."""
    dictionary = FolderItems(folderpath)
    dir_list = os.listdir(folderpath)

    for key1, value1 in Keyword.items():
        if all_items is True:
            for key, value in dictionary.items():
                for emotions, data in dict(value).items():
                    if emotions == key1:
                        dictionary[key][emotions] = (value1+data)/2

        elif dictionary.get(key1) is None:
            dictionary[key1] = Keyword.get(key1)
        
        else:
            here = [i for i in list(value1) if i in list(dictionary[key1])]
            not_here = [i for i in list(value1) if i not in list(dictionary[key1])]
            
            if len(here)>0:
                for data in here:
                    val1 = dict(dictionary[key1]).get(data)
                    val2 = dict(Keyword[key1]).get(data)
                    
                    dictionary[key1][data] = (val1+val2)/2

            for data in not_here:
                dictionary[key1][data] = Keyword[key1][data]
                
        
    for interval, file in enumerate(dir_list):
        with open(f"{folderpath}\{file}", "w") as f:
            json.dump(DataSpread.slice(dictionary, interval), f, indent=2)


if __name__ == '__main__':
    string = "libs"
    dir_list = os.listdir("libs")
    print(len(GrabJsonData("piss.json")))
    
    
    