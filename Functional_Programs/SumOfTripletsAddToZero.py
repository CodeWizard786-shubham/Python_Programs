"""
@Author: shubham shirke
@Date: 2022-06-02 17:54:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 17:54:30
@Title : program to find triplets that sum to exactly zero from a N number series.
"""

def find_triplets_of_sum_zero(num):
    """
    Description : The function reads in N integers (positive and negative) and counts the
                  number of triples that sum to exactly 0.
    Parameters  : num specifies the number of integers to read in.
    result      : count of triplets and triplets that add up to zero 
    """
    triplets = []
    count = 0
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
                    count += 1

    return count, triplets


num = int(input("Enter the number of integers: "))
arr = []
for i in range(num):
    integer = int(input(f"Enter an integer{i+1}: "))
    arr.append(integer)

count, triplets = find_triplets_of_sum_zero(arr)

print("Number of distinct triplets: ", count)
print("Distinct triplets:")
for i in triplets:
    print(i)
