def print_logo():
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

def get_name():
    return input("What is your name? ")

def get_bid():
    while True:
        bid = input("What's your bid? $")
        try:
            bid = int(bid)
            if bid < 1:
                print("Please enter a positive number")
                continue
            break
        except:
            print("Please enter a valid number")
    return bid

def get_others_exist():
    while True:
        inp = input("Are ther any other bidders? Type 'yes' or 'no': ").lower()
        if inp == 'yes':
            return True
        elif inp == 'no':
            return False
        print("Please type 'yes' or 'no'")

def create_dict():
    bidders = {}
    while True:
        name, bid = get_name(), get_bid()
        bidders[name] = bid
        if not get_others_exist():
            break
    return bidders

def get_winner(bidders):
    highest_bid = 0
    highest_name = ''

    for key, value in bidders.items():
        if value > highest_bid:
            highest_bid = value
            highest_name = key
    return [highest_name, highest_bid]

def run():
    print_logo()
    print("Welcome to the secret auction program")
    bidders = create_dict()
    winner = get_winner(bidders)
    print(f"The winner is {winner[0]} with a bid of {winner[1]}!")

run()