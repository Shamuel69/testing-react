import json
import os
from tibs.Classes import WordNotFound

class Helper:

    def thea_represent(file, *args):
        "Simply a helper function to append the files to the args"
        if type(file) == list:
            list(file).extend(args)
        
        elif type(file) == str:
            file = [file]
            file.append(args)
        
        elif type(file) == dict:
            dict(file).update(args)
        
        return file

    def find_item(file=None, *args, word:str, path=""):
        "this is for user interface. NOT INTEDED FOR USE"
        file = Helper.thea_represent(file, args)
        
        try:
            for item in file:
                with open(f"{path}\{item}") as f:
                    data = json.load(f)
                
                for key in data:
                    if key == word:
                        return print(f"Found the word, *{key}* ~ {item}")

        except FileNotFoundError:
            for item in file:
                with open(f"{item}") as f:
                    data = json.load(f)
                
                for key in data:
                    if key == word:
                        return print(f"Found the word, *{key}* ~ {item}")

        except:
            raise WordNotFound(word)
    
    def find_new(old: list, pop: list):
        "check if there is any new items when comparing 2 list"
        val = [i for i in pop if i in old]
        
        for iter in val:
            old.pop(iter)
        
        return old

    def temp_file(filename:str, item:dict):
        "Probably creates a file based around your input"
        try:
            with open(f"{filename}") as f:
                data = json.load(f)
            
            for key, emotion in item.items():
                data[key] = emotion

        except:
            with open(f"{filename}", "w") as f:
                f.write("{}")
            
            with open(f"{filename}") as f:
                data = json.load(f)
            
            for key, emotion in item.items():
                data[key] = emotion

        with open(f"{filename}", "w") as f:
            json.dump(data, f, indent=2)
    
    def locate_final_file(folderpath: str):
        dir_list = os.listdir(folderpath)
        
        return sorted(dir_list)

if __name__ == '__main__':
    string = "libs"
    # intents = intents["intent"]
    # if intents in list(data.keys()):
    #     data[intents]["inputs"] += [inputs]
    #     data[intents]["response"] = response
    
    # else: 
    #     data[intents] = {}
    #     data[intents]["inputs"] = list(inputs)
    #     data[intents]["response"] = response
    