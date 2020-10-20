class Matrix():

    def solve(self, matrix, row, col):
        # Проверка на заполнение всех полей
        if not matrix:
            return ('Заполните матрицу')
        elif not row:
            return ("Введите номер строки")
        elif not col:
            return ("Введите номер столбца")
        else:
            # двумерный массив в виде n строк, каждая из которых содержит m чисел, разделенных пробелами
            input_matrix = [[int(j) for j in input().split()] for i in range(row)]
            # номер строки и столбца для обмена
            input_row = int(input()) - 1
            input_col = int(input()) - 1
            # return [matrix, input_row, input_col]

            # Заполняем вектор верхних значений
            top_vector = input_matrix.shift()

            # Заполняем вектор боковых значений
            side_vector = []
            for row in input_matrix:
                side_vector.push(row.shift())

            # Оставшаяся матрица - матрица значений
            matrix = input_matrix

            # Меняем указанные строки и столбцы в матрице
            result = self.jordan(matrix, input_row, input_col)

            # Меняем указанные строки и столбцы у векторов боковых и верхних значений
            cup = side_vector[input_row]
            if (top_vector[input_col] == 0):
                side_vector[input_row] = top_vector[input_col]
            else:
                side_vector[input_row] = top_vector[input_col].substring(1)
            if (cup == 0):
                top_vector[input_col] = cup
            else:
                top_vector[input_col] = '-' + cup

            # Убираем лишние нули из вектора верхних значений
            top_vector = lst = [list(filter(None, lst)) for lst in top_vector]

            # Выводим ответ
            self.output(result, top_vector, side_vector)

    def output(self, matrix, top_vector, side_vector):
        # Строка на вывод с начальным отступом
        temp_string = "     "

        #Заполняем заголовок
        for i in range(top_vector):
            temp_string += "   " + top_vector[i]

        #Заполняем матрицу
        for i in range(len(matrix)):
            # Новая строка матрицы
            temp_string += "\n"
            # Пишем заголовок строки
            temp_string += side_vector[i]
            if (side_vector[i] == 0):
                temp_string += "    "
            else:
                temp_string += "   "
            # Пишем числа матрицы
            for j in range(len(matrix[i])):
                if (matrix[i][j] >= 0) :
                    temp_string += " "
                temp_string += " " + matrix[i][j].toFixed(2)

        # Выводим получившуюся строку
        return temp_string

    def delete_column(self, a, n):
        # a - массив, где удаляем строку
        # r - номер колонки, которую удаляем
        new_arr = []
        for i in range(len(a)):
            new_arr[i] =[]
            row = a[i]
            for j in range(len(row)):
                if j != n:
                    new_arr[i].push(row[j])
        return new_arr

    def jordan(self, matrix, row, column):
        temp_matrix = []
        # Пересчитываем всю матрицу
        for i in range(len(matrix)):
            temp_matrix[i] =[]
            for j in range(len(matrix[i])):
                temp_val = (matrix[i][j] * matrix[row][column] - matrix[i][column] * matrix[row][j]) / matrix[row][column]
                temp_matrix[i][j] = temp_val
        # Пересчитываем столбец
        for i in range(len(matrix)):
            temp_matrix[i][column] = matrix[i][column] / matrix[row][column] * -1

        # Пересчитываем строку
        for i in range(len(matrix[row])):
            temp_matrix[row][i] = matrix[row][i] / matrix[row][column]

        # Пересчитываем указанное значение
        temp_matrix[row][column] = 1 / matrix[row][column]

        # Удаляем обнулившееся значение
        temp_matrix = self.delete_column(temp_matrix, column)
        return temp_matrix



