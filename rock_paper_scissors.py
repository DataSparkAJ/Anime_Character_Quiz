import random
'''
1 for rock
-1 for paper
0 for scissor
'''
computer = random.choice([-1, 0, 1])
you_str = input("Enter your choice: ")
youDict = {"R": 1, "P": -1, "S": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}
you = youDict[you_str]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer == you):
    print("Shit! It's a draw.😐")
else:

    if(computer == -1 and you == 0):
        print("Congrats You Win!🥳 ")
    elif(computer == -1 and you == 1):
        print("So Sad, You Lose!😭")

    elif(computer == 1 and you == 0):
        print("So Sad, You Lose!😭")
    elif(computer == 1 and you == -1):
        print("Congrats You Win!🥳 ")

    elif(computer == 0 and you == -1):
        print("So Sad, You Lose!😭")
    elif(computer == 0 and you == 1):
        print("Congrats You Win!🥳 ")

    else:
        print("Your game is trash!👎")


