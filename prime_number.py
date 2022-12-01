import math

def is_prime_number(x):
    if x<=1:
        print(error)
    else:
        for i in range(2, x):
            if x % i ==0:
                return False
        return True
    
print(is_prime_number(1))
print(is_prime_number(4))
print(is_prime_number(7))
print(is_prime_number(17))
print(is_prime_number(45))
