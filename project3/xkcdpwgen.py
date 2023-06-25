import argparse
import random

with open('./words.txt', 'r') as f:
    words = f.read().lower().split('\n')

parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
parser.add_argument('-w', '--words', type=int, default=4,
                    help='include WORDS words in the password (default=4)')
parser.add_argument('-c', '--caps', type=int, default=0,
                    help='capitalize the first letter of CAPS random words (default=0)')
parser.add_argument('-n', '--numbers', type=int, default=0,
                    help='insert NUMBERS random numbers in the password (default=0)')
parser.add_argument('-s', '--symbols', type=int, default=0,
                    help='insert SYMBOLS random symbols in the password (default=0)')

args = parser.parse_args()

selected = random.sample(words, k=args.words)
capitalized = random.sample(list(range(args.words)), k=args.caps)
for i in capitalized:
    selected[i] = selected[i].capitalize()
selected += random.choices([str(i) for i in range(10)], k=args.numbers)
selected += random.choices([*'~!@#$%^&*.:;'], k=args.symbols)
random.shuffle(selected)
print(''.join(selected))
