import time

print("Hello, I am ChatChetan.")
time.sleep(1)
print("I am an AI made to chat with you.")
time.sleep(1)

name = input("What should I call you? ")
time.sleep(1)

print(f"{name}, that is a nice name.")
time.sleep(1)

mood = input("How are you feeling today? good bad unsure ").lower()
time.sleep(1)

if mood == "good":
    print("That is great to hear. I like when people feel good.")
elif mood == "bad":
    print("I am sorry you feel that way. I am here to talk if you want.")
elif mood == "unsure":
    print("It is okay to not know. Feelings can be confusing.")
else:
    print("I understand. Humans feel many things at once.")

time.sleep(1)

chat = input("Do you want to keep talking with me? yes no ").lower()

if chat == "yes":
    topic = input("What do you want to talk about? ")
    print(f"Interesting. I like talking about {topic}.")
    time.sleep(1)
    print("I could talk about it for hours but I will stop here.")
else:
    print("Alright. I will let you rest.")

time.sleep(1)
print(f"It was nice chatting with you, {name}. Farewell.")