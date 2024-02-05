# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

my_arr = np.array([input().split()], dtype=int)
# print(my_arr)
print(np.reshape(my_arr, (3, 3)))
