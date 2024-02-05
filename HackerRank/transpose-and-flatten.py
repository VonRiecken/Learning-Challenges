# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

m_size = input()
N = int(m_size[0])
M = int(m_size[2])

arr = np.array([input().split() for i in range(N)], dtype=int)

print(np.transpose(arr))
flat_arr = arr.flatten()
print(flat_arr)
