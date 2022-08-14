#ROCK PAPER SCISSORS
import itempng
import random

print(itempng.logo)
print(" ")

user = int(input("Type 0 for rock, 1 for Paper, 2 for scissors"))

if user == 0:
    print(itempng.Rock)
elif user == 1:
    print(itempng.Paper)  
elif user == 2:
    print(itempng.Scissors)
else:
    print("invalid")  

options = [itempng.Rock,itempng.Paper,itempng.Scissors]   
computer = random.randint(0,len(options)- 1 ) 

if computer == 0:
    print(itempng.Rock)
elif computer == 1:
    print(itempng.Paper)  
elif computer == 2:
    print(itempng.Scissors)

if user == 0 and computer == 2:
    print("you win")
elif user == 2 and computer == 0:
    print("you loose")
elif computer > user :
    print("you loose")
elif user > computer:
    print("you win")    
elif computer == user:
    print("draw")           



