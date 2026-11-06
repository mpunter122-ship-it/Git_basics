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

def dotprod(x,y):
    return np.dot(x.T, y)

print(dotprod(vec_1,vec_2))


def is_prime(n): 
    for i in range(2,n):
        if n % i == 0:
            return False
    return True 
            
print("7 is prime is a", is_prime(7), "statement")

