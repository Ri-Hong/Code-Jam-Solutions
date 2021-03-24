'''
Author: Ri Hong
Date Solved: March 24, 2021
Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
'''

#Explanation
'''
For this problem, we have to do three things:
1) Get the 'trace' which is the sum of all the values along the diagonal from the top left to the bottom right of the matrix
2) In each row, check if any elements are duplicated and get the total number of rows that have duplicated values
3) In each column, check if any elements are duplicated and get the total number of column that have duplicated values

To get the trace, we can simply iterate from 0 to the size of the matrix on a variable i. Then we simply sum up the value located
at the ith row and ith column every time.

To check if a row contains duplicated values, loop through the row and for each element, store it in a list. Before we store it, we will
check if our current element already exists inside the list. If so, then that row contains duplicated elements. 

Perform the same procedure on the columns to get the number of columns with duplicated values
'''

numCases = int(input())

for caseNum in range(numCases):
    #Construct the matrix
    matrix = [] #stores the values in the matrix as a 2D array
    gridSize = int(input())
    for row in range(gridSize):
        matrix.append(list(map(int, input().split())))
        
    #Calcualte Trace
    trace = 0
    for i in range(gridSize):
        trace += matrix[i][i]

    #Calculate Duplicated Rows
    numRowDupes = 0
    for row in range(gridSize):
        alreadyCounted = []
        for col in range(gridSize):
            if matrix[row][col] in alreadyCounted:
              numRowDupes += 1
              break
            else:
              alreadyCounted.append(matrix[row][col])

    #Calculate Duplicated Columns
    numColsDupes = 0
    for col in range(gridSize):
        alreadyCounted = []
        for row in range(gridSize):
            if matrix[row][col] in alreadyCounted:
              numColsDupes += 1
              break
            else:
              alreadyCounted.append(matrix[row][col])



    print("Case #{}: {} {} {}".format(caseNum+1, trace, numRowDupes, numColsDupes))