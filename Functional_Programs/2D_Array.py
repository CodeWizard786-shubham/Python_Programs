"""
@Author: shubham shirke
@Date: 2022-06-02 17:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 13:03:30
@Title : Generate a 2D array of M (columns) and N (Rows).
"""

def two_d_array(M , N):
    """
    Description : A library for reading in 2D arrays of integers, doubles, or booleans from
                  standard input and printing them out to standard output.
    parameter : M - Number of Rows , N - Number of columns
    return : two dimentional array of size M * N
    """
    arr = [[0 for j in range(N)] for i in range(M)]
    
    # Read input values for each cell of the array
    for i in range(M):
      for j in range(N):
        arr[i][j] = input(f"Enter value for row {i+1}, col {j+1}: ")
    # Print out the values of the array from each cell
    for i in range(M):
       for j in range(N):
          print(arr[i][j],end=" ")
       print()

rows =eval(input("Enter number of rows: "))
cols =eval(input("Enter number of Columns: "))
print("The 2-D array : ")
two_d_array(rows,cols)