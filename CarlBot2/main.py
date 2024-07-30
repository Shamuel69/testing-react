

sentences = []
ignore_characters = ["?", "!", ".", ","]


class Lemmitizer():
    #words > numbers > most common numbers
    def __init__(self, input:str):
        self.Tokenized = self.word_splitter(input)

    def word_splitter(self, words:str) -> list[str]:
        words = words.lower()
        for characters in ignore_characters:
            if words.find(characters) >=1:   
                words = words.replace(characters, "")         

        return words.split()

def lemmitizer(input: str, max_length:int):
    if len(input)>= max_length:
        return "Sorry I cannot lemmitize this: (too many characters)"
    
    
    

if __name__=='__main__':
    stink = input()
    print(Lemmitizer(stink).Tokenized)
