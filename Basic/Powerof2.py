"""
@Author: shubham shirke
@Date: 2023-06-02 18:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 14:03:30
@Title : Compute the power of 2 series.
"""

def power_of_two(num):
    if(num!=31):
        for i in range(1,num):   
            power_of_num=2**i
            print(power_of_num)
    else:
            print("Enter number less than 31")

num = int(input("Enter the value of N: "))
power_of_two(num)
