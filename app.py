from Matrix import Matrix

solve = Matrix()

matrix = int(input('Введите кол-во строк в матрице и заполните ее '))
row = int(input())
col = int(input())

M = solve.solve(matrix, row, col)

print(M)