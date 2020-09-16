# TO-DO: complete the helper function below to merge 2 sorted arrays
# partition function <<<<<<<
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    arrA_index = 0
    arrB_index = 0
    merged_arr_index = 0
    #check whether both arrays have values
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        #if value at index of arrA> value at index of arrB
        if arrA[arrA_index] > arrB[arrB_index]:
        #replace value at index of merged_arr with the value at index of arrB
            merged_arr[merged_arr_index] = arrB[arrB_index]
            merged_arr_index += 1
            arrB_index += 1
        else:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index += 1
            arrA_index += 1
        #check if arrA is empty, if it is dump values of arrB into sortes array ??????????
    if arrA_index == len(arrA): #<<<< ???????????????? how it is checking the empty?
        for item in arrB[arrB_index:]:
            merged_arr[merged_arr_index] = arrB[arrB_index]
            merged_arr_index +=1
            arrB_index += 1
#check if the array is empty, if it is  dump values of arr A into sorted array
    if arrB_index == len(arrB):
        for item in arrB[arrA_index:]:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index +=1
            arrA_index += 1

    return merged_arr

print(merge([3,4], [1,5]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # Recursively split the array in half until len(all arrays) == 1
    if len(arr) > 1:
        # define midpoint
        m = len(arr) // 2
        # define left half
        l = arr[:m]
        # define right half
        r = arr[m:]

        # Recurse left half
        l = merge_sort(l)
        # Recurse right half
        r = merge_sort(r)

        # Setup pointers for merge
        i = 0  # Traverses left arr
        j = 0  # Traverses right arr
        k = 0  # Traverses arr for inserting values into sorted location
        # Iterate through l and r simultaneously,
        # find smallest value between current index in l and r
        # and insert it at arr[k], inc k as you go
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        # Cleanup left over elements from uneven arr's
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

