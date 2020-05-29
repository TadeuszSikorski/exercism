class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self) -> bool:
        try:
            numbers = [int(number) for number in "".join(self.card_num.split())]

            if len(numbers) <= 1:
                return False
            else:
                numbers.reverse()
        except ValueError:
            return False

        for index, number in enumerate(numbers):
            if index % 2 != 0:
                numbers[index] *= 2

                if numbers[index] > 9:
                    numbers[index] -= 9

        return sum(numbers) % 10 == 0
