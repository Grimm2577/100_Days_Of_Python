# Day 4 finally underwraps! actually had to think about the best way to write this without having an overly long file of code, and even then
# I really do think i could shorten this by quite a bit in the future

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Creating a list for the available moves
move_set = [rock, paper, scissors]

# Selecting a random move from the moves list
computer_selected_move = random.choice(move_set)

# Receiving the selected move from the player
select_move = input("What do you choose? 0, 1 Or 2: ")

# Creating a default variable for comparing the moves inside the algorithm
selected_move = 0

# Checking if the players move is rock
if select_move == "0":
    print(rock)

    # Printing the computers move
    print("Computer Chose:")
    print(computer_selected_move)

    # Settiing the default variable to the selected move
    selected_move = int(select_move)

    # Comparing if the selected move is rock then paper and finally scissors to output the match results
    # Using the index for the random choice of the array and comparing it to the integer of the player selected move
    if selected_move == move_set.index(computer_selected_move):
        print("Draw!")
    elif move_set.index(computer_selected_move) == 1:
        print("You lost!")
    else:
        print("You Win!")

# Checking if the players move is paper
elif select_move == "1":
    print(paper)

    # Printing the computers move
    print("Computer Chose:")
    print(computer_selected_move)

    # Settiing the default variable to the selected move
    selected_move = int(select_move)

    # Comparing if the selected move is paper then rock and finally scissors to output the match results
    # Using the index for the random choice of the array and comparing it to the integer of the player selected move
    if selected_move == move_set.index(computer_selected_move):
        print("Draw!")
    elif move_set.index(computer_selected_move) == 0:
        print("You Win!")
    else:
        print("You Lost!")

# Checking if the players move is scissors
elif select_move == "2":
    print(scissors)

    # Printing the computers move
    print("Computer Chose:")
    print(computer_selected_move)

    # Settiing the default variable to the selected move
    selected_move = int(select_move)

    # Comparing if the selected move is scissors then paper and finally rock to output the match results
    # Using the index for the random choice of the array and comparing it to the integer of the player selected move
    if selected_move == move_set.index(computer_selected_move):
        print("Draw!")
    elif move_set.index(computer_selected_move) == 1:
        print("You Win!")
    else:
        print("You Lost!")


else:
    print("Invalid Move!")