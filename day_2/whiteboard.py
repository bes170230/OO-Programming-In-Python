# Squared and Sorted Array
# Write a function that takes a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order 
# Sample Input:
# Array = [1,2,3,5,6,8,9]
# Sample Output:
# [1,4,9,25,36,64,81]
# Sample Input2:
# Array = [-9,-3,1,2,5,6,8]
# Sample Output2:
# [1,4,9,25,36,64,81]#

Array = [1,2,3,5,6,8,9]
Array_2 = [-9,-3,1,2,5,6,8]

def squared(x):
    return x**2

def array_squared(array):
    squared_array = sorted(map(squared,array))
    return squared_array 

print(array_squared(Array_2)) 