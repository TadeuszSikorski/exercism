class Matrix:
    def __init__(self, matrix_string):
        if type(matrix_string) != str:
            raise Exception("The argument provided must be a string.")

        self.matrix = [list(map(int, row.split())) for row in matrix_string.split("\n")]

    def row(self, index):
        self.check_entered_arg(index)

        self.row_of_matrix = []

        for column_index in range(len(self.matrix[index - 1])):
            self.row_of_matrix.append(self.matrix[index - 1][column_index])

        return self.row_of_matrix

    def column(self, index):
        self.check_entered_arg(index)

        self.column_of_matrix = []

        for row_index in range(len(self.matrix)):
            self.column_of_matrix.append(self.matrix[row_index][index - 1])

        return self.column_of_matrix

    def check_entered_arg(self, arg):
        if type(arg) != int:
            raise Exception("The argument provided must be an integer.")
