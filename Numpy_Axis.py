import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Sum along columns (axis=0)
column_sum = np.sum(matrix, axis=0)
print("Column Sum:")
print(column_sum)
# [ 12 15 18 ]

# Sum along rows (axis=1)
row_sum = np.sum(matrix, axis=1)
print("Row Sum:")
print(row_sum)
# [ 6 15 24 ]

