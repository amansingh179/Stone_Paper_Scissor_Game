import random

user_score=0
computer_score=0

select=["stone","paper","scissor"]

while True:
    user_input=input("Type Stone/Paper/Scissor or Q to quit: ")

    user_input=user_input.lower()
    if user_input=="q":
        print("Ok Bye!")
        break

    if user_input not in select:
        continue

    random_selection=random.randint(0,2)
    computer_select=select[random_selection]
    print("Computer Picked : ",computer_select,"!\n")

    if user_input == "stone" and computer_select == "scissor":
        print("You won!\n")
        user_score += 1

    elif user_input == "paper" and computer_select == "stone":
        print("You won!\n")
        user_score += 1

    elif user_input == "scissor" and computer_select == "paper":
        print("You won!\n")
        user_score += 1

    else:
        print("You lost!\n")
        computer_score += 1  

    print("You won", user_score, "times.\n")
    print("The computer won", computer_score, "times.\n")
    print("Goodbye!")
        
    
    
        