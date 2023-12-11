import random

def rock():
    return '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

def paper():
    return '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

def scissors():
    return '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def print_drawing(n):
    if n == 0:
        print(rock())
    elif n == 1: print(paper())
    else: print(scissors())

def game():
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    choice = int(input())
    if choice < 3:
        print_drawing(choice)
    else: return 'This choice doesn\'t exist'

    comp_choice = random.randint(0,2) 
    print("Computer chose:")
    print_drawing(comp_choice)
    wins = [[0, 2], [2, 1], [1, 0]]
    if [choice, comp_choice] in wins:
        return "You Win!"
    elif choice == comp_choice:
        return "It's a tie"
    else:
        return "You Lose!"

print(game())