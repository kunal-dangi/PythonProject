import pandas

data = pandas. read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows ()}
print(phonetic_dict)

for letter, code in phonetic_dict.items():
    word = input("Enter a word: "). upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry please enter a valid word")
    else:
        print(output_list)
        break
