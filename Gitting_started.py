import numpy as np

def factorial(n):
    x = 1
    for i in range(1,n+1):
        x = i*x
    return x
def factorial2(n): 
    if n == 0:
        return 1
    return n*factorial2(n-1) 

vec_1 = np.array([1,2,3])

vec_2 = np.array([4,5,6])

vec_3 = vec_1 + vec_2
exit()

print(vec_3)

