class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, row.split())) for row in matrix_string.split("\n")]

    def row(self, index):
        self.row_of_matrix = []

        for column_index in range(len(self.matrix[index - 1])):
            self.row_of_matrix.append(self.matrix[index - 1][column_index])

        return self.row_of_matrix

    def column(self, index):
        self.column_of_matrix = []

        for row_index in range(len(self.matrix)):
            self.column_of_matrix.append(self.matrix[row_index][index - 1])

        return self.column_of_matrix
