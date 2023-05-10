import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

word = input("Enter a word: ")

phonetic_code = {row.letter: row.code for (index, row) in data.iterrows()}
print([phonetic_code[letter.upper()] for letter in word])
