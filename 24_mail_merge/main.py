with open("input/letters/starting_letter.txt") as letter_text:
    # letter is a string with the letter content
    letter = ''.join(letter_text.readlines())

with open("Input/Names/invited_names.txt") as name_text:
    # names is a list with all the name and "\n" at the end of every name
    names = name_text.readlines()

for i in range(len(names)):
    # we're removing "\n" at the end of every name because we don't want to go to a new line
    stripped = names[i].strip("\n")
    f = letter.replace('[name]', stripped)
    # saving the final letter in this path. if the file doesn't exist, python will create that file and save it
    with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt", mode='w') as final_latter:
        final_latter.write(f)