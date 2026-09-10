import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code = data["code"]

alpha = data["letter"]
# print(code)
# print(alpha)

dict = {key:value for key,value in zip(alpha,code)}   # zip() is used for merging 2 lists or string etc... together
#what you can use here as well if zip() is confusing is
#{row.letter:row.code for (index,row) in data.iterrows()}
# print(dict)

word = input("Enter a word: ").upper()

output = [dict[key] for key in word]
print(output)
