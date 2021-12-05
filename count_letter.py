import argparse
import string
vowel_list=["a", "e", "i", "o", "u", "y"]
parser = argparse.ArgumentParser()
parser.add_argument("string", type=str, help="prints out a list of letters in alphabetical order with the number of occurrences")
parser.add_argument("-v", "--vowel", action="store_true", help="shows vovewls only")
parser.add_argument("-c", "--consonant", action="store_true", help="shows consonants only")
args = parser.parse_args()
answer = (args.string).lower()

if args.vowel and args.consonant:
    for letter in string.ascii_lowercase:
        print(letter, answer.count(letter))
elif args.vowel:
    print("a", answer.count('a'))
    print("e", answer.count('e'))
    print("i", answer.count('i'))
    print("o", answer.count('o'))
    print("u", answer.count('u'))
    print("y", answer.count('y'))
elif args.consonant:
    for letter in string.ascii_lowercase:
        if letter in vowel_list:
            continue
        print(letter, answer.count(letter))
else:
    for letter in string.ascii_lowercase:
        print(letter, answer.count(letter))