class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны быть одинакового размера!!!")
        result = Matrix(self.rows, self.columns)
        for i_row in range(self.rows):
            for j_column in range(self.columns):
                result.data[i_row][j_column] = self.data[i_row][j_column] + other.data[i_row][j_column]
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны быть одинакового размера!!!")
        result = Matrix(self.rows, self.columns)
        for i_row in range(self.rows):
            for j_column in range(self.columns):
                result.data[i_row][j_column] = self.data[i_row][j_column] - other.data[i_row][j_column]
        return result

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!!!")
        result = Matrix(self.rows, other.columns)
        for i_row in range(self.rows):
            for j_column in range(other.columns):
                for i_column in range(self.columns):
                    result.data[i_row][j_column] += self.data[i_row][i_column] * other.data[i_column][j_column]
        return result

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[j][i] = self.data[i][j]
        return result

    def __str__(self):
        output = ""
        for row in self.data:
            output += "\t".join(str(element) for element in row)
            output += "\n"
        return output


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
