import random
import json
import pickle
import numpy as np
#your gonna have to make all of this again, this time revisit how to tokenize shit
import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model
from Code_Libraries.log import Log, timefunc
from Code_Libraries.Protocolmain import ProtoFunc

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("homemade classifier/libraries/sentences.json").read())

words = pickle.load(open("homemade classifier/Pickles and models/words.pkl", "rb"))
classes = pickle.load(open("homemade classifier/Pickles and models/classes.pkl", "rb"))
model = load_model("homemade classifier/Pickles and models/Carl_bot.model")
print(words)
print(classes)
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    print(f"\n++++++++++++++++++++\n\nsentence words 1: {sentence_words}")
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    print(f"sentence words 2: {sentence_words}")
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag= [0]* len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            print(f"bag word vs word: {word} | {w}")
            if word == w:
                bag[i] = 1
                print(f"copied word: {word}")
    
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    print(f"bag of words: {bow}")
    res = model.predict(np.array([bow]))[0]
    print(f"res: {res}")
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    print(f"result: {result}")

    result.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in result:
        return_list.append({"intent": classes[r[0]], "probablilty": str(r[1])})
    print(f"return_list: {return_list}")
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    print(f"tag: {tag}")
    print(f"list of intents: {list_of_intents}")
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i["responses"])
            break
        
    return result

def helper_data(data:dict, intents):
    return data[intents]["inputs"]

def insert_text(inputs, intents, response:str):
    with open("homemade classifier\libraries\inputs.json", "r") as f:
        data = json.load(f)
    
    intents = intents["intent"]

    try:    
        assert len(data[intents].keys()) >= 2
        data[intents]["inputs"] += [inputs]
        data[intents]["response"] = response
    except:
        data[intents] = {}
        data[intents]["inputs"] = [inputs] 
        data[intents]["response"] = response

    with open("homemade classifier\libraries\inputs.json", "w") as f:
        json.dump(data, f, indent=2)



User = []
robotres = ""
logs = Log()
interval = 0
protofuncs = ["repeat (user)", "repeat (machine)", "RUN FILE", "All .EXE", "Google Search", "IP", "Where am I", "Coordinates", ""]
while True:
    # study how the machine gets to the tag it needs, if proto func is in the first 3 then sep them
    
    if interval < 1:
        User.append(logs.PullData())
        interval += 1
    
    message = input(f": ")

    ints = predict_class(message)
    
    if (ints[0]["intent"] in protofuncs) and (User != "DEFAULT"):
        # try:
            robotres=str(ProtoFunc(ints[0], message, user=User, robot_response=robotres))
            print("CarlBot: "+robotres+"\n===========================\n")
        # except:
        #     error_json = open("homemade classifier\libraries\errors.json", "w")
        #     print(f"Im sorry, I cannot fulfill that request\n{Exception.__name__}\n===========================\n")

    else:
        res = get_response(ints, intents)
        robotres=res
        print("CarlBot: "+res+"\n===========================\n")

    insert_text(message, ints[0], robotres)