import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_code = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
  word = input("Enter a word: ")

  try:
    output_list = [phonetic_code[letter.upper()] for letter in word]
  except KeyError:
    print("sorry, only letter in the alphabet please") 
    generate_phonetic()
  else:
    print("output_list")
generate_phonetic()
