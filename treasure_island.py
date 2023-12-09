def game():
    print('''*******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************''')

    print('Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou\'re at a cross road. Where do you want to go? Type "left" or "right" ')
    left_right = input()
    if left_right == 'right': 
        return "You fell into a hole. Game Over."
    elif left_right != 'left':
        return "You chose a direction that doesn't exist. Game Over."

    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    wait_swim = input()
    if wait_swim == 'swim':
        return "You get attacked by an angry trout. Game Over."
    elif wait_swim != 'wait':
        return "You chose an action that doesn't exist. Game Over."
    
    print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ')
    color = input()
    if color == 'red':
        return "It's a room full of fire. Game Over."
    elif color == 'blue':
        return "You enter a room of beasts. Game Over."
    elif color == 'yellow':
        return "You found the treasure! You Win!"
    else:
        return "You chose a door that doesn't exist. Game Over."

print(game())