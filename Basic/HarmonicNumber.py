"""
@Author: Author Name
@Date: 2023-06-02 18:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 14:03:30
@Title : To find the nth harmonic number.
"""
def harmonic_number_series(num):
    sum=0
    if(num > 0):
        for i in range(1,num+1):
            harmonic_number = 1/i 
            harmonic_number_sum = sum + harmonic_number
        print("The nth term of hramonic series: ",harmonic_number_sum)
    else:
        print("enter number greater than 0")

num =int(input("Enter the Nth number: "))
harmonic_number_series(num)
