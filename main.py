"""
1 for snake 
-1 for water
0 for gun
"""

import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youStr]

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# By now we have 2 numbers (variables), you and computer

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if computer == you:
    print("Draw!")

# compu - you
else:
# if computer - you becomes -1 or 2 it means you win analytically

    if((computer - you) == -1 or (computer - you) == 2):
        print("You loose!")
    else:
        print("You win!")


#     if computer == -1 and you == 1: 
#         print("You win!")

#     elif computer == -1 and you == 0: 
#         print("You lose!")

#     elif computer == 1 and you == -1: 
#         print("You loose!")

#     elif computer == 1 and you == 0: 
#         print("You win!")

#     elif computer == 0 and you == 1: 
#         print("You loose!")

#     elif computer == 0 and you == -1: 
#         print("You win!")

#     else:
#         print("Something went wrong!")

