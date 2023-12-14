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
    
def get_inputs():
    enc_or_dec = 'p'
    while enc_or_dec not in ['e', 'd']:
        enc_or_dec = input("Type 'e' to encrypt, type 'd' to decrypt: ")
    
    string = input("Type your message: ")
    
    number = ''
    while type(number) is not int:
        try:
            number = int(input("Type the shift number: "))
        except:
            continue

    return [enc_or_dec, string, number]

def encode(string, number):
    result = ''
    for char in string:
        order = ord(char)
        new_order = order + number
        while new_order > 122:
            new_order -= 26
        result += chr(new_order)
    return result

def decode(string, number):
    result = ''
    for char in string:
        order = ord(char)
        new_order = order - number
        while new_order < 97:
            new_order += 26
        result += chr(new_order)
    return result

def run():
    print_logo()
    inputs = get_inputs()
    if inputs[0] == 'e':
        print(f"Encoded message is: {encode(inputs[1], inputs[2])}")
    else:
        print(f"Decoded message is: {decode(inputs[1], inputs[2])}")
run()