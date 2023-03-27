"""
Write a program that parses a sentence and
replaces each word with the following: first letter, number of distinct characters between first and
last character, and last letter. Words are separated by spaces or non-alphabetic characters and
these separators should be maintained in their original form and location in the answer.

Examples:
1. “Smooth” becomes “S3h”
2. “Space separated” becomes “S3e s5d”
3. “Dash-separated” becomes “D2h-s5d”
4. “Number2separated” becomes “N4r2s5d”
"""

import re

def parse_word(word: str) -> str:
    first_letter = word[0]
    last_letter = word[-1]
    letter_count = len(set(word[1:-1]))
    result = f"{first_letter}{letter_count}{last_letter}"
    return result

def parse_sentence(sentence: str) -> str:
    pattern = r"[^A-Za-z]"
    if re.search(pattern, sentence) is not None:
        sep_index = re.search(pattern, sentence).start()
        sep = str(sentence[sep_index])
        words = [parse_word(word) for word in sentence.split(sep)]
        result = sep.join(words)
    else:
        result = parse_word(sentence)
    return result

if __name__ == "__main__":
    sentence = "Smooth"
    result = parse_sentence(sentence)
    print(result)

    sentence = "Space separated"
    result = parse_sentence(sentence)
    print(result)

    sentence = "Dash-separated"
    result = parse_sentence(sentence)
    print(result)

    sentence = "Number2separated"
    result = parse_sentence(sentence)
    print(result)
