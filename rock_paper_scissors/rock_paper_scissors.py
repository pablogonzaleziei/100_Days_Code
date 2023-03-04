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

#Write your code below this line 👇
import random
game=[rock,paper,scissors]
human = int(input("Type 0 for rock, 1 for paper or 2 for scissors "))
computer = random.randint(0,2)
print("Human chose: \n")
print(game[human])
print("\nComputer chose: \n")
print(game[computer]) 

if computer == 0:
    print(rock)
    if human == 0:
        print("TIE")
    elif human == 1:
        print("HUMAN WINS")
    elif human == 2:
        print("COMPUTER WINS")
if computer == 1:
    print(paper)
    if human == 0:
        print("COMPUTER WINS")
    elif human == 1:
        print("TIE")
    elif human == 2:
        print("HUMAN WINS")
if computer == 2:
    print(scissors)
    if human == 0:
        print("HUMAN WINS")
    elif human == 1:
        print("COMPUTER WINS")
    elif human == 2:
        print("TIE")

