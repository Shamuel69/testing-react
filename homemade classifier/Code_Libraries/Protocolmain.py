from steam.client import SteamClient
from steam.steamid import SteamID
from Code_Libraries.log import Log
from Code_Libraries.location import Location
from Code_Libraries.search import Search


client = SteamClient()


def games(title: str, SteamUsername: str, SteamPassword: str):
    
    client.cli_login(SteamUsername, SteamPassword)
    print(int(SteamID.account_id))
    #get the list of games from account


class ProtoFunc:
    def __init__(self, prediction:dict, *args, **kwargs):
        intent = prediction["intent"]
        location = Location()

        profile = kwargs["user"][0]
        LocWithData = Location(profile)
        
        if intent == "IP":
            self.response = f"Here you go! {location.get_ip()}"

        if intent == "Where am I":
            loc_info = dict(location.location_info)
            city = loc_info["name"]
            country = loc_info["country"]
            self.response = f"Based off your IP Adress, you are around {city} {country}\n\n"

        if intent == "Coordinates":
            if profile.get("number") == None:
                answer = input(f"{location.IP_cords}, I couldn't get your IDEAL coordinates because I don't have your phone number. Would you be interested in sharing it?\n\n")

                if answer in ["yes", "sure", "I can do that", "yeah"]:
                    answer = input("Well go on.")
                    if str(answer).isnumeric():
                        profile["number"] = answer
                        Log.InsertIntoProf(profile, profile["name"])
                        
                        self.response = f"Great! your coordinates are {LocWithData.averaged_location}\n\n"
                
                else:
                    if str(answer).isnumeric():
                        profile["number"] = answer
                        Log.InsertIntoProf(profile, profile["name"])

                        self.response = f"Great! your coordinates are {LocWithData.averaged_location}\n\n"

            else:
                self.response = f"I averaged your coordinates and this is what I came up with, {location.averaged_location}\n\n"
                
        
        if intent == "repeat (user)":
            self.response = 'You said, "%s"' % args
        
        if intent == "repeat (machine)":
            self.response =  'I said, "%s"' % kwargs["robot_response"]

        if intent == "Google Search":
            self.response = "Here are some links to help you find what your looking for:\n\n    {0}\n\n".format(Search(args).results)

        if intent == "RUN FILE":
            question = input("what game would you like me to run?\n\n")
            UserPass = Log.SteamLogin(kwargs["name"])
            games(question, UserPass[0], UserPass[1])
    
    def __str__(self) -> str:
        return self.response

        


if __name__=='__main__':
    ProtoFunc({"intent": "IP"}, "samuel parnell")
