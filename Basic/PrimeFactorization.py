"""
@Author: shubham shirke
@Date: 2023-06-02 14:08:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 14:08:30
@Title : Computes the prime factorization of N using brute force.
"""

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i)
            n =n // i
        else:
            i += 1
    if n > 1:
        print(n)

num = int(input("Enter a number: "))
print("Prime factors of", num, "are:")
prime_factors(num)