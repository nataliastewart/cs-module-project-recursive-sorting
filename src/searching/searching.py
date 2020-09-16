# TO-DO: Implement a recursive implementation of binary search



def binary_search(arr, target, start, end):

    # start = 0
    # end = len(arr) - 1

    if end >= start:
        mid = (end + start) // 2

        #if the element is present at the middle itself
        if arr[mid] == target:
            return mid
            #if the element is smaller than mid, then it can only
            #be present in left(start) subarray
        elif arr[mid] > target:
                #We gonna search to the left side (start)
            return binary_search(arr, target, start, mid - 1)
        else:
                #move to the right side (end)
            return binary_search(arr, target, mid + 1, end )
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

