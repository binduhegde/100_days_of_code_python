import pandas as pd
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df = pd.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for index, row in df.iterrows()}

while True:
    user_inp = input("Enter a word: ").upper()
    try:
        result = [data_dict[i] for i in user_inp]
        break
    except KeyError:
        print("Please enter letters only")
print(result)