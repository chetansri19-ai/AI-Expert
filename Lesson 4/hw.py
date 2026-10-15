import random

moves=["rock","paper","scissors"]

def ai_random():
    return random.choice(moves)

def winner(p,a):
    if p==a:
        return "draw"
    if (p=="rock" and a=="scissors") or (p=="paper" and a=="rock") or (p=="scissors" and a=="paper"):
        return "player"
    return "ai"

def game():
    p_score=0
    a_score=0
    print("Rock Paper Scissors with AI")
    print("Choose: rock, paper, scissors")
    print("Type exit to stop")

    while True:
        p=input("You: ").lower()
        if p=="exit":
            print("Final Score:",p_score,"-",a_score)
            break
        if p not in moves:
            print("Invalid")
            continue

        a=ai_random()
        result=winner(p,a)

        print("AI:",a)
        if result=="player":
            p_score+=1
            print("You win")
        elif result=="ai":
            a_score+=1
            print("AI wins")
        else:
            print("Draw")

        print("Score:",p_score,"-",a_score)

game()