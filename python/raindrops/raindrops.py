def convert(number: int) -> str:
    if type(number) != int:
        raise Exception("The argument provided must be an integer.")

    raindrops = ""

    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        raindrops = "{}".format(number)

    return raindrops
