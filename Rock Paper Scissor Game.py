"""

Workflow of project:
1- Input from user(Rock,Paper,Scissor)
2- Computer choice (Computer will choose randomly not conditionlly)
3- Result print

Cases :
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B- Paper
Paper - Rock = Paper Win
Paper - Paper = Tie
Paper - Scissor = Scissor Win

C- Scissor
Scissor - Paper = Scissor Win
Scissor - Rock = Rock Win
Scissor - Scissor = Tie

"""

import random
item_list = ["Rock","Paper","Scissor"]
 
User_Choice = input("Enter your move = Rock,Paper,Scissor :")
Computer_Choice = random.choice(item_list)

print(f"User choice = {User_Choice}, Computer Choice = {Computer_Choice}")

if User_Choice == Computer_Choice:
    print("Both chooses same : Match Tie")
    
elif User_Choice == "Rock":
    if Computer_Choice == "Paper":
        print("Paper covers Rock : Computer Win")
    else:
        print("Rock smashes scissor : You Win")    
        
elif User_Choice == "Paper":
    if Computer_Choice == "Rock":
        print("Paper cover Rock : You Win")
    else:
        print("Scissor cut Paper : Computer Win")
         
elif User_Choice == "Scissor":
    if Computer_Choice == "paper":
        print("Scissor cut Paper : You Win")
    else:
        print("Rock Smashes Scissor : Computer Win")
    











