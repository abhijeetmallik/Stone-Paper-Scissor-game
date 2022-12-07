import random
print("WELCOME TO ROCK PAPER SCISSOR GAME")

user_score = 0
comp_score = 0
ties = 0

name= input("Enter your Name: ")
print("""
Winning Rules are:
1. Paper vs Rock --> Paper
2. Rock vs Scissor --> Rock
3. Scissor vs Paper --> Scissor""")
print()
while True:
    print("""Choices are:
    1. Rock
    2. Paper
    3. Scissor""")
    choice = int(input("Enter your Choice: "))
    print()
    while choice>3 or choice<1:
        choice= int(input("Enter Valid Input"))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"
    print("Your Choice is:",user_choice)
    print("Now it's Computer's Turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"
    print("The Computer's Choice is:",comp_choice)

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper Wins!")
        result = "Paper"
    elif ((user_choice == "Scissor" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissor")):
        print("Rock Wins!")
        result = "Rock"
    elif (user_choice == comp_choice):
        print("It's a Tie")
        result = "Tie"
    else:
        print("Scissor Wins!")
        result = "Scissor"
    if result == "Tie":
        ties +=1
    elif result == user_choice:
        print("You won!")
        user_score +=1
    else:
        print("Computer Won!")
        comp_score +=1
    print("Scores are")
    print(name,"'s Score is:",user_score)
    print("Computer's Score is:",comp_score)
    print("Ties are",ties)

    repeat =input("Do you want to play again? ")
    if repeat == "no" or repeat == "No" or repeat == "NO":
        print("Game Over!")
        print("Thanks for playing!!!")
        break