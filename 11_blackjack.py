import random

def print_logo():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/ """)

def get_random_card():
    options = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(options)

# randomly keeps adding numbers to the computer's cards 
# until the sum is no longer less than 17. it's a rule
def get_computers_cards():
    cards = []
    while sum(cards) < 17:
        cards.append(get_random_card())
    return cards

# returns a boolean value. True if the player wants to 
# get another card and False otherwise
def get_another_card():
    while True:
        inp = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
        if inp == 'yes': return True
        elif inp == 'no': return False
        print("Please type 'yes' or 'no'")

# gets 2 cards for the user to begin with
def get_starting_user_cards():
    return [get_random_card() for i in range(2)]

def get_winner(user_score, comp_score):
    if user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😁"
    elif user_score == comp_score:
        return "It's a draw 😐" 
    else:
        return "You lose 😭"

def play_game():
    user_cards = get_starting_user_cards()
    computer_cards = get_computers_cards()

    while sum(user_cards) < 22: #exits the whil loops when the sum of user card goes beyond 21
        print(f"\nYour cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # breaks the while loop if the player doesn't want to get another card
        if not get_another_card():
            break 
        
        user_cards.append(get_random_card())
    
    user_sum, comp_sum = sum(user_cards), sum(computer_cards)
    print(f"\nYour final hand: {user_cards}, Your final score: {user_sum}")
    print(f"Computer's final hand: {computer_cards}, Computer's final score: {comp_sum}")

    return [user_sum, comp_sum]

def run():
    print_logo()
    print("Welcome to the game of blackjack!")
    
    game_scores = play_game()
    user_sum, comp_sum = game_scores[0], game_scores[1]
    print(get_winner(user_sum, comp_sum))
run()