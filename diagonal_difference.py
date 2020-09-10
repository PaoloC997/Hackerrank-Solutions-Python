


def diagonalDifference(arr):
    # Write your code here
   
    sum_first_diagonal = sum(arr[i][i] for i in range(n))
    sum_second_diagonal = sum(arr[i][n -i -1] for i in range(n))
    pres = (int(sum_first_diagonal) - int(sum_second_diagonal))
    
    return abs(pres)