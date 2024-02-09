import random
choices = ("rock", "paper", "scissor")
while True:
    n= input("Enter your choice:")
    if n == "end":
        print("Thanks")
        break
    computer = random.choice(choices)
    print("Your choice:",n)
    print("Computer choice:",computer)
    if n == computer:
        print("It's a tie!")
    elif (n== "rock" and computer == "scissor") or(n == "scissor" and computer== "paper") or (n== "paper" and computer== "rock"):
        print("You win")
    else:
        print("Computer wins")
