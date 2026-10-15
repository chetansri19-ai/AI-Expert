import re
import random
from colorama import Fore, init
init(autoreset=True)

destinations={
    "beaches":["Bali","Maldives","Phuket","Gold Coast","Fiji"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas","Blue Mountains"],
    "cities":["Tokyo","Paris","New York","Singapore","Dubai"]
}

weather_tips={
    "hot":["Pack light cotton clothes","Bring sunscreen","Carry a reusable water bottle"],
    "cold":["Pack warm layers","Carry gloves and a beanie","Bring thermal socks"],
    "rainy":["Carry an umbrella","Pack waterproof shoes","Bring a raincoat"]
}

budget_ranges={
    "low":["Bangkok","Bali","Phuket"],
    "medium":["Tokyo","Paris","Singapore"],
    "high":["Swiss Alps","Maldives","Dubai"]
}

jokes=[
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

personality_modes={
    "friendly":"😊 Friendly Mode Activated!",
    "sarcastic":"😏 Sarcastic Mode Activated!",
    "professional":"📘 Professional Mode Activated.",
    "excited":"🔥 HYPER‑EXCITED MODE ACTIVATED!!!"
}

current_mode="friendly"
user_name=""

def normalize(t):
    return re.sub(r"\s+"," ",t.strip().lower())

def respond(t):
    global current_mode
    if current_mode=="friendly":
        print(Fore.GREEN+f"TravelBot: {t}")
    elif current_mode=="sarcastic":
        print(Fore.YELLOW+f"TravelBot: Oh wow, {t}. Amazing.")
    elif current_mode=="professional":
        print(Fore.CYAN+f"TravelBot: {t}.")
    elif current_mode=="excited":
        print(Fore.MAGENTA+f"TravelBot: {t.upper()}!!!")

def recommend():
    respond("Beaches, Mountains, Cities, or say 'surprise me'")
    pref=normalize(input(Fore.YELLOW+f"{user_name}: "))
    if pref=="surprise me":
        cat=random.choice(list(destinations.keys()))
        sug=random.choice(destinations[cat])
        respond(f"Random pick: {sug}")
        return
    if pref in destinations:
        sug=random.choice(destinations[pref])
        respond(f"How about {sug}? yes or no")
        ans=normalize(input(Fore.YELLOW+f"{user_name}: "))
        if ans=="yes":
            respond(f"Enjoy {sug}")
        else:
            respond("Trying again")
            recommend()
    else:
        respond("I don't have that category")

def packing_tips():
    respond("Where are you going")
    loc=normalize(input(Fore.YELLOW+f"{user_name}: "))
    respond("How many days")
    days=normalize(input(Fore.YELLOW+f"{user_name}: "))
    respond("Weather type (hot/cold/rainy)")
    w=normalize(input(Fore.YELLOW+f"{user_name}: "))
    respond(f"Packing tips for {days} days in {loc}")
    print(Fore.GREEN+"- Pack versatile clothes")
    print(Fore.GREEN+"- Bring chargers/adapters")
    print(Fore.GREEN+"- Check the weather forecast")
    if w in weather_tips:
        for tip in weather_tips[w]:
            print(Fore.GREEN+f"- {tip}")

def budget_recommend():
    respond("Budget level (low/medium/high)")
    lvl=normalize(input(Fore.YELLOW+f"{user_name}: "))
    if lvl in budget_ranges:
        sug=random.choice(budget_ranges[lvl])
        respond(f"Try visiting {sug}")
    else:
        respond("Invalid budget level")

def tell_joke():
    respond(random.choice(jokes))

def change_mode():
    global current_mode
    respond("Choose mode: friendly, sarcastic, professional, excited")
    m=normalize(input(Fore.YELLOW+f"{user_name}: "))
    if m in personality_modes:
        current_mode=m
        respond(personality_modes[m])
    else:
        respond("Unknown mode")

def show_help():
    print(Fore.MAGENTA+"\nI can:")
    print(Fore.GREEN+"- recommend")
    print(Fore.GREEN+"- packing")
    print(Fore.GREEN+"- budget")
    print(Fore.GREEN+"- joke")
    print(Fore.GREEN+"- mode")
    print(Fore.CYAN+"Type 'exit'\n")

def detect_intent(t):
    t=normalize(t)
    intents={
        "recommend":["recommend","suggest","destination","travel"],
        "packing":["pack","packing","bag","luggage"],
        "budget":["budget","cheap","expensive","cost"],
        "joke":["joke","funny","laugh"],
        "mode":["mode","personality","style"],
        "help":["help","commands"],
        "exit":["exit","bye","quit"]
    }
    for intent,keys in intents.items():
        if any(k in t for k in keys):
            return intent
    return "unknown"

def chat():
    global user_name
    print(Fore.CYAN+"Hello I'm TravelBot")
    user_name=input(Fore.YELLOW+"Your name: ")
    respond(f"Nice to meet you {user_name}")
    show_help()
    while True:
        u=input(Fore.YELLOW+f"{user_name}: ")
        intent=detect_intent(u)
        if intent=="recommend":
            recommend()
        elif intent=="packing":
            packing_tips()
        elif intent=="budget":
            budget_recommend()
        elif intent=="joke":
            tell_joke()
        elif intent=="mode":
            change_mode()
        elif intent=="help":
            show_help()
        elif intent=="exit":
            respond("Safe travels goodbye")
            break
        else:
            respond("I didn't understand")

if __name__=="__main__":
    chat()