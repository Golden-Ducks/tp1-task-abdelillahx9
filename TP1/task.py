D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 =  "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."



num_words = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}


def remove_punctuation(text):
    punctuations = ".,!?;:"
    for char in punctuations:
        text = text.replace(char, "")
    return text


def normalize_text(text):
    text = text.lower()

    text = remove_punctuation(text)

    words = text.split()

    for i, word in enumerate(words):
        if word in num_words:
            words[i] = num_words[word]

    return " ".join(words)






D1_norm = normalize_text(D1)
D2_norm = normalize_text(D2)
D3_norm = normalize_text(D3)
D4_norm = normalize_text(D4)

print(D1_norm)
print(D2_norm)
print(D3_norm)
print(D4_norm)