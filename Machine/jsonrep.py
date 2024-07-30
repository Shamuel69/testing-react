import json

class jsoninput:
    def __init__(self, file: str, tempfile:str, data: dict):
        with open(f"{file}") as f:
            file = json.load(f)
        
        pos = p

        print(fac)
        with open(tempfile, "w") as d:
            json.dump(file, d, index=4)

