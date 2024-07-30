import json
import random
import time

def timefunc(func):
    def wrapper():
        t1 = time.process_time()
        func()
        print(f"took {t1} seconds to complete")
    return wrapper

profiles = json.loads(open("homemade classifier/libraries/usernames.json").read())

class Log:
    def __init__(self):
        self.Users = self.PullNames()
        self.User_profiles = profiles["profiles"]

    @staticmethod
    def PullNames() -> list:
        prof_list = profiles["profiles"]
        Users = []
        for title in prof_list:
            Users.append(title["name"])
        
        return Users
        
    def InsertIntoProf(self, kwargs: dict, name):
        for iter, data in enumerate(self.User_profiles):
            if data["name"] == name:
                self.User_profiles.pop(iter)
                self.User_profiles.append(kwargs)
                
                with open("homemade classifier/libraries/usernames.json", "w") as f:
                    json.dump(self.User_profiles, f, indent=2)

                return
    
    def questionsolved(answer, **data):
        if answer in ["yes","sure","yeah", "okay"]: 
            new_profile = {}
            new_profile["name"] = data["name"] 

            list(data["User_profiles"]).append(new_profile)
            profiles["profiles"] = data["User_profiles"]

            with open("homemade classifier/libraries/usernames.json", "w") as f:
                json.dump(profiles, f, indent=2)
            
            return new_profile["name"]
        
        else:
            return "DEFAULT"
        

    def PullData(self) -> dict:

        start_phrase = ["Who is using the robot?\n\n%s\n\n", "I was sleeping... What's your name?\n\n%s\n\n", "Who's there?\n\n%s\n\n"]
        end_phrase1 = ["Hi %s! what can I do for you?\n\n", "Hey %s! Is there anything I can help you with?\n\n", "Wassup %s! What are we working on today?\n\n","Welcome %s! How can I help you today?\n\n"]
    
        name = input(f"{random.choice(start_phrase)}" % self.Users)
        name_stored = name
        name = name.lower().replace(" ", "").split()
        for i, itername in enumerate(self.Users):
            if name[0] in itername:
                
                print(f"{random.choice(end_phrase1)}" % name_stored)
                return self.User_profiles[i]
                
        end_phrase2 = ["Nice to meet you %s! Is there anything I can help you with?\n\n", "Great meeting you %s! What are we working on today?\n\n", "Nice to meet you %s! What can I do for you?\n\n", "Pleasure to meet you %s! What can I assist you with?\n\n"]
        answer = input("It appears your name isn't in my database, would you like me to add you?\n\n")

        print(f"{random.choice(end_phrase2)}" % name_stored)
        return Log.questionsolved(answer, User_profiles= self.User_profiles, name=name)

    def SteamLogin(name:str):
        UserPass = []
        prof_list = profiles["profiles"]
        for i in prof_list:
            dataname = i["name"]        
            if dataname == name:
                for w in i["steam"]:
                    
                    if i["steam"][w] == "blank":
                        username = input("I do not have your username or password, may you please type your username in?\n\n")
                        password = input("Now the password, don't worry this is private.\n\n")

                        UserPass.append(username)
                        UserPass.append(password)
                        i["steam"]["username"] = username
                        i["steam"]["password"] = password
                        
                        with open("homemade classifier/libraries/usernames.json", "w") as f:
                            json.dump(profiles, f, indent=2)
                        return UserPass
                    
                    UserPass.append(i["steam"]["username"])
                    UserPass.append(i["steam"]["password"])
                    return UserPass

if __name__ == '__main__':
    # logs = log()

    print(Log().Users)
    
    # PullProfiles()
    # log.questionsolved("sam", log.PullProfiles()[1], "wumbo")
    # log.SteamLogin("samuel parnell")