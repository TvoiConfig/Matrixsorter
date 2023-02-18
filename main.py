import numpy as np

m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))
v = int(input("Максимальное значение ячейки: "))
matrix = np.random.randint(v, size = (m, n))
print("Выдана матрица:\n", matrix)

max = np.amax(matrix, axis = 0)
min = np.amin(matrix, axis = 0)

for i1 in range(m):                           
    for  i2 in range(n):
        if matrix[i1, i2] == max[i2]:           
            matrix[i1, i2] = min[i2]
        elif matrix[i1, i2] == min[i2]:
            matrix[i1, i2] = max[i2]

print("Преобразованная матрица:\n", matrix)