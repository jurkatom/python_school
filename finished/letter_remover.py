import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string", type=str, help="base string")
parser.add_argument("letter", type=str, help="cutouted letter")
args = parser.parse_args()
answer = args.string
cutout = args.letter

for letter in answer:
    if letter==cutout:
        continue
    print(letter, end="")