import time
from pprint import pprint
from random import randint

# matrix_size = 3

# matrix_a = [
#     [ 3,  1, -4 ],
#     [ 2, -3,  1 ],
#     [ 5, -2,  0 ]
# ]

# matrix_b = [
#     [ 1, -2, -1 ],
#     [ 0,  5,  4 ],
#     [ -1, -2, 3 ]
# ]

# matrix_r = [
#     [ 0, 0, 0 ],
#     [ 0, 0, 0 ],
#     [ 0, 0, 0 ]
# ]

matrix_size = 20

matrix_a = [[0] * matrix_size for i in range(matrix_size)]

matrix_b = [[0] * matrix_size for i in range(matrix_size)]

matrix_r = [[0] * matrix_size for i in range(matrix_size)]

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix[row][col] = randint(-5, 5)

start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    matrix_r = [[0] * matrix_size for i in range(matrix_size)]
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix_r[row][col] += matrix_a[row][i] * matrix_b[i][col]
    print(matrix_a)
    print(matrix_b)
    print(matrix_r)
    print() 
end = time.time()           
print("Done, time taken : ", end - start)