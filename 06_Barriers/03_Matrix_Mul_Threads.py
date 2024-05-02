import time
from pprint import pprint
from random import randint
from threading import Barrier, Thread

#######################
# FUNCTION DEFINITION #
#######################

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix[row][col] = randint(-5, 5)
                
def work_out_row(row):
    while True:
        work_start.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix_r[row][col] += matrix_a[row][i] * matrix_b[i][col]
        work_complete.wait()

########
# MAIN #
########

matrix_size = 20
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)

matrix_a = [[0] * matrix_size for i in range(matrix_size)]
matrix_b = [[0] * matrix_size for i in range(matrix_size)]

for row in range(matrix_size):
    th = Thread(target = work_out_row, args = ([row]))
    th.start()

start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    matrix_r = [[0] * matrix_size for i in range(matrix_size)]
    work_start.wait()
    work_complete.wait()

end = time.time()            
print("Done, time taken : ", end - start)