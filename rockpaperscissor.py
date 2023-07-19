import random

user_wins = 0
comp_wins = 0
tie_games = 0

options = ["rock", "paper", "scissors"]
while(1):
    user_input = input("type rock/paper/scissors or Q to quit: ").lower()
    if (user_input == "q"):
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    # 0-rock 1-paper 2-scissor
    comp_choice = options[random_num] 
    print("Computer picked", comp_choice + ".")

    if user_input == "rock" and comp_choice == "scissors":
        print("User wins")
        user_wins += 1
        

    elif user_input == "paper" and comp_choice == "rock":
        print("User wins")
        user_wins += 1
        

    elif user_input == "scissors" and comp_choice == "paper":
        print("User wins")
        user_wins += 1
        

    elif user_input == comp_choice:
        print("It's a tie! Try again.")
        tie_games = tie_games + 1
       
    else:
         print("Comp wins")
         comp_wins += 1

print("You won", user_wins,"times")
print("Comp won", comp_wins, "times")
print("goodbye!")
      