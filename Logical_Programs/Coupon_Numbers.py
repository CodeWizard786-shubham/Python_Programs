"""
@Author: shubham shirke
@Date: 2022-06-03 10:36:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-03 10:36:30
@Title : Python program to generate N number of 9 digit unique coupon codes.
"""

import random

def generate_unique_coupons(number_of_coupons):
    """
    Description : The function generates 9 digit unique coupons
    Parameters : number_of_coupons - Number of 9 digit unique coupons want to be generarted.
    result : random_coupon_list 
    """
    arrlist = []
    i=0
    while (i < number_of_coupons):
        number = random.randint(100000000, 999999999)  # Generates a random 9-digit number
        if(is_unique(number)):               #check if the number is unique, if unique store in list
            arrlist.append(number)
            i +=1
        if(i >= number_of_coupons):
            break
    return arrlist

def is_unique(number):      # The function checks for unique digits in a coupon using set and returns true or false 
    digits = set(str(number))
    return len(digits) == len(str(number))

#Prints each coupon from the coupon list.
def print_coupon_list(random_coupon_list):
    for coupons in random_coupon_list:
        print(coupons)


# main
def main():
    number_of_coupons = int(input("Enter number of coupons needed: "))
    random_coupon_list=generate_unique_coupons(number_of_coupons)
    print_coupon_list(random_coupon_list)


if __name__=="__main__":
   main()
