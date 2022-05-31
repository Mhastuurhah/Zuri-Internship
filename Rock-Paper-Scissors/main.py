from random import choice
print("\nWelcome to Rock Paper Scissors\n")
print("Instructions" )
print("---------------------\n Enter: ")
print("""'R' for 'rock'\n'P' for 'paper'\n'S' for 'scissors'""")
print("---------------------")

option = ["R", "P", "S"]
dic_options = {"R":"Rock", "P":"Paper", "S":"Scissors"}
flag = True
while flag:
    user_input = input("Pick an option btw 'R', 'P', and 'S': ")
    if user_input not in option:
        print("Not an option, pick again.")
        continue
    else:
        comp_input = choice(option)
        print(f"Player({dic_options[user_input]}) : CPU({dic_options[comp_input]})")
        if user_input == comp_input:
            print("It's a tie, Play Again!!!")
            continue
        elif user_input == "R":
            if comp_input == "P":
                print("Paper covers Rock!\nComputer wins, You lose!\nGame Over!")
                flag = False
            else:
                print("Rock smashes Scissors!\nYou win!\nGame Over!")
                flag = False
        elif user_input == "P":
            if comp_input == "S":
                print("Scissors cuts Paper!\nComputer wins, You lose!\nGame Over!")
                flag = False
            else:
                print("Paper covers Rock!\nYou win!\nGame Over!")
                flag = False
        elif user_input == "S":
            if comp_input == "R":
                print("Rock smashes Scissors!\nComputer wins, You lose!\nGame Over!")
                flag = False
            else:
                print("Scissors cuts Paper!\nYou win!\nGame Over!")
                flag = False


