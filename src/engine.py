import json
import os
import random


def read_letter_file(fn):
    with open(fn) as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f'problem at parse json file {fn}: {e}')
            return
        try:
            letter = data['letter']
            unicode_hexadecimals = data['unicode_hexadecimals']
        except Exception as e:
            print(f'problem at file struct {fn}: {e}')
            return
        return letter, unicode_hexadecimals


def read_letters_data():
    letters_data = {}
    data_path = "letters_data"
    files = os.listdir(data_path)
    for file in files:
        letter, hex_strings = read_letter_file(os.path.join(data_path, file))
        if letter in letters_data:
            print(f'letter {letter} already read')
            continue
        letter_analogs = []
        for h_str in hex_strings:
            try:
                character = chr(int(h_str, base=16))
            except Exception as e:
                print(f'can not decode {h_str}')
                continue

            letter_analogs.append(character)
        letters_data[letter] = letter_analogs
        print(f'{letter} {", ".join(letter_analogs)}')
    return letters_data


def translate(letters_data, input: str, choice_number=None):
    subst_letters = []
    for letter in input.lower():
        if letter in letters_data:
            choices = letters_data[letter]
            if choice_number and len(choices) > choice_number:
                subst_letter = choices[choice_number]
            else:
                subst_letter = random.choice(choices)
            subst_letters.append(subst_letter)
        else:
            subst_letters.append(letter)
    return ''.join(subst_letters)


if __name__ == '__main__':
    letters_data = read_letters_data()
    inpt = input("Type your name:")
    for number in range(len(set(inpt))):
        print(translate(letters_data, inpt, number))
