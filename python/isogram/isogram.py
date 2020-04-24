def is_isogram(string: str) -> bool:
    if len(string) > 0:
        string = string.lower()
    else:
        return True

    letters = generate_letters_dict(string)
    result = False

    for letter in letters:
        if len(letters) != 0 and letters[letter] > 1:
            result = False
            break
        else:
            result = True

    return result


def generate_letters_dict(string: str) -> dict:
    letters = {}
    counter = 0

    for letter in string:
        if letter != " " and letter != "-":
            letters[letter] = 0

    for character in string:
        for letter in letters:
            if character == letter:
                counter += 1
                letters[letter] += counter
        counter = 0

    return letters
