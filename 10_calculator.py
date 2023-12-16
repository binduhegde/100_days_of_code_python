def print_art():
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)

def add(a, b):
    return a+b

def multiply(a,b):
    return a * b

def subtract(a,b):
    return a-b

def division(a,b):
    return round(a/b, 4)

# This makes sure that the user put in a number and converts it into float
def take_float_input(message):
    while True:
        inp = input(message)
        try:
            inp = float(inp)
            break
        except ValueError:
            print("Plase enter a valid number")
    return inp

# This takes the operation sign (+,-,*,/) from the user and makes sure the user inputs a valid sign
def get_operation():
    print("+\n-\n*\n/")
    while True:
        op = input("Pick an operation: ")
        if op in '+-*/':
            return op
        print("Please type in a valid operation")

# This does the calculations by using the functions above and returns the ans
def do_operation(operation, a, b):
    if operation == "+":
        ans = add(a, b)
    elif operation == "-":
        ans = subtract(a, b)
    elif operation == '*':
        ans = multiply(a, b)
    else:
        ans = division(a, b)
    return ans

# This asks the use if they want to continue to calculate with the answer. outputs a boolen value
def continue_or_not(n):
    while True:
        inp = input(f"Do you want to continue calculating with {n}? Type yes or no: ")
        if inp == 'yes': return True
        elif inp == 'no': return False
        else:
            print("Please type 'yes' or 'no'")

def run():
    print_art()
    num1 = take_float_input("What's the first number?: ")
    
    while True:
        operation = get_operation() # gets the valid sign
        num2 = take_float_input("What's the second number?: ")

        ans = do_operation(operation, num1, num2)
        print(f"{num1} {operation} {num2} = {ans}")

        if not continue_or_not(ans): # breaks while loop if the user enters no
            break
        num1 = ans # if the user wants to continue calculating with the ans, that ans becomes num1
run()
