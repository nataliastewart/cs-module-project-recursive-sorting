# TO-DO: complete the helper function below to merge 2 sorted arrays
# partition function <<<<<<<
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    pivot = arr[0]
    left = []
    right = []
    # Your code here
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    #we have elements on left (array), pivot(array) and right(array)
    return left, pivot, right
    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #base case : in the len array <= 1
    if len(arr) <= 1:
        return arr


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

