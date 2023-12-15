def print_logo():
    print('''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')
    
def get_operation_type():
    while True:
        operation_type = input("Type 'e' to encrypt, type 'd' to decrypt: ")
        if operation_type in ['e', 'd']:
            return operation_type
        else:
            print("Invalid input. Please type 'e' to encrypt or 'd' to decrypt.")

def get_message():
    return input("Type your message: ")

def get_shift_amount():
    while True:
        try:
            shift_amount = int(input("Type the shift number: "))
            return shift_amount
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift.")

def encrypt(message, shift):
    result = ''
    for char in message:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            
            # 'ord(char) - offset': ord(char) - 65 if it's uppper else 97
            # 'ord(char) - offset + shift': Applies the shift value to the character position. 
            # '(ord(char) - offset + shift) % 26': to make sure for the shift value + char 
            #       doesn't go beyond the letter z. it wrapes around
            # '(ord(char) - offset + shift) % 26 + offset': Returns the shifted character's 
            #       position back to the ascii value within the alphabet range.
            # 'chr((ord(char) - offset + shift) % 26 + offset)': Converts the shifted ascii 
            #       value back to the corresponding character.
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char # doesn't encode or decode anything other than alphabet
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def run_cipher():
    print_logo()
    
    operation_type = get_operation_type()
    message = get_message()
    shift = get_shift_amount()

    if operation_type == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encoded message is: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift)
        print(f"Decoded message is: {decrypted_message}")

run_cipher()
