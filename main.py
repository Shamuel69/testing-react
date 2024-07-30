
from Machine.commas import itentify, Tokenize, Determiners
from Machine.Math import Calculate
from statistics import median

class split_sent:
    def __init__(self, input_var: str):
        
        data = {"positive": 0, "negative": 0}

        input_var = itentify(input_var).commas
        input_var = input_var.replace(",",".").replace("'","").replace(":",".").replace(";",".").replace("{",".").replace("}",".").replace("(",".").replace(")",".")
        self.sep_sentences = input_var.split(".")

        stripper = Determiners(self.sep_sentences)
        self.strip = stripper.text
        self.suffix = stripper.suffix_strip()
        
        self.sep_spaces = Tokenize(self.sep_sentences).split
        
        scrapper = Calculate(self.sep_sentences)

        self.posneg = scrapper.data
        self.coll_data = scrapper.collection(data)
        

    def words(self):
        return self.suffix

    def indi_words(self):
        return self.sep_spaces
    
    def sent_data(self):
        return self.posneg

if __name__ == '__main__':
    # sentence = "I boil cats"

    # sentence = split_sent(sentence)
    
    
    # print(sentence.suffix)

    def practice(amount:int):
        max = 50
        list_primes = [2, 3, 5, 7, 11, 13]
        string = "i"
        middle = "o"
        maps = list(map(lambda x: amount%x, list_primes))

        numb_zeros = maps.count(0)
        numb_counted = []
        for i, k in enumerate(maps):
            if k == 0:
                numb_counted.append(i)
        
        
        numb_counted = list_primes[numb_counted[-1]]
        
        print(numb_counted)
        Height = amount/numb_counted
        

        counting = 0
        list_strings = ""

        for i in range(40):
            if counting >=numb_counted:
                list_strings += "\n"
                counting = 0 
            
            list_strings += "i"
            counting += 1
            print((list_strings))
        

    # message = input("you: ")
    # print(message)
    print((practice(20)))