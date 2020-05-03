def score(word: str) -> int:
    letter_values = (
        (("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"), 1),
        (("D", "G"), 2),
        (("B", "C", "M", "P"), 3),
        (("F", "H", "V", "W", "Y"), 4),
        (("K"), 5),
        (("J", "X"), 8),
        (("Q", "Z"), 10),
    )

    score = 0

    for letter in word.upper():
        for letters, value in letter_values:
            for character in letters:
                if letter == character:
                    score += value

    return score
