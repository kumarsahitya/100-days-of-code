PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contenets = letter_file.read()
    for name in names:
        new_letter = letter_contenets.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)