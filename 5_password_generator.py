import random

def get_password():
    print("Welcome to the PyPassword Generator!\n\
          How many letters would you like in your password?")
    no_letters = int(input())
    print("How many symbols would you like? ")
    no_symbols = int(input())
    print("How many numbers would you like?")
    no_numbers = int(input())

    letters = [chr(random.randint(65, 90)) for i in range(no_letters)]+ \
        [chr(random.randint(97, 122)) for j in range(no_letters)]
    letters = random.sample(letters, no_letters)

    symbols = [chr(random.randint(33, 47)) for i in range(no_symbols)]

    numbers = [str(random.randint(0,9)) for i in range(no_numbers)]

    combined = letters + symbols + numbers
    random.shuffle(combined)

    print("Your password is: ", end='')
    return ''.join(combined)
print(get_password())
