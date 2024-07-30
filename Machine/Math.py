import json


class Calculate:
    def __init__(self, data: list):
        with open("Machine/Data/posneg.json") as f:
            file = json.load(f)

        positives = file["positives"]
        negatives = file["negatives"]

        posneg = {"positive": 0, "negative": 0}
        
        for list_words in data:
            list_words = str(list_words).split(" ")
            for word in list_words:
                
                if word in positives:
                    posneg["positive"] += 1

                if word in negatives:
                    posneg["negative"] += 1
                    print(word)

        self.data = posneg

    def collection(self, data: dict):
        posneg = self.data

        pos = posneg["positive"]
        neg = posneg["negative"]

        data["positive"] += pos
        data["negative"] += neg

        return data

