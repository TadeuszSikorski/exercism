class Matrix:
    def __init__(self, matrix_string):
        if type(matrix_string) != str:
            raise Exception("The argument provided must be a string.")

        self.matrix = [list(map(int, row.split())) for row in matrix_string.split("\n")]

    def row(self, index):
        self.__check_entered_arg(index)

        return self.matrix[index - 1]

    def column(self, index):
        self.__check_entered_arg(index)

        return [row[index - 1] for row in self.matrix]

    def __check_entered_arg(self, arg):
        if type(arg) != int:
            raise Exception("The argument provided must be an integer.")
