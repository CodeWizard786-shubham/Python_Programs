"""
@Author: shubham shirke
@Date: 2022-06-02 20:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 20:03:30
@Title : calculate euclidean distance to origin.
"""

import math

def find_euclidean_distance(x,y):
    """
    Description: The function calculates euclidean distance between (x,y) coordinates to origin (0,0) using math.sqrt function
    Parameters : x - first coordinate and y - second coordinate
    result : distance between coordinates and origin in type float.
    """
    distance = math.sqrt(x**2 + y**2)      # calculate distance
    return distance

# Read x and y coordinate from user
x_coordinate = eval(input("Enter X coodrinate: "))
y_coordinate = eval(input("Enter Y coodrinate: "))

distance =find_euclidean_distance(x_coordinate,y_coordinate)

# print distance 
print(f"The distance from {x_coordinate,y_coordinate} to origin {0,0} is : ",distance)



