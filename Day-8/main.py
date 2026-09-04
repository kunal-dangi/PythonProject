
PLACEHOLDER = "[name]"

with open("invited_guests.txt","r") as names:
    names = names.readlines()

with open("./INPUT/letter.txt","r") as letters:
    letters = letters.read()



for name in names:
        clean_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, clean_name)

        with open(f"letter_for_{clean_name}.txt", "w") as letter:
            letter.write(new_letter)