from precision import Precision as p
from numpy.random import randint

def bubble_sort(arr: list) -> list:

    for k in range(len(arr)):   #iterate over list at most k times
        swap_tracker = False    #initialize swap checker, records if swap is made

        for i in range(len(arr)-k-1):             # if k = 0 (initial pass), then loop from 0-> len(arr)-1. on next pass, loop from len(arr)-2, and so on

            if arr[i] > arr[i+1]:                 # if current array element is greater than next array element, list out of order
                arr[i], arr[i+1] = arr[i+1], arr[i] #swap em
                swap_tracker = True                #record that a swap was made

        if swap_tracker == False:                 #if a pass completes with no swaps being made, list is sorted
            break

    return arr                                    #return sorted list


A = [p(randint(-100,100)) for i in range(0,5)] #list of random numbers between -100, 100, converted to our high precision data type

out = bubble_sort(A)                        #sort da list
print([str(out[i]) for i in range(len(A))]) #print out string representations

def merge(left :list , right:list) -> list: 
    merged_list = [] 
    i = j = 0 # pointers here

    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            merged_list.append(left[i])
            i = i + 1 #increment the counter to check the next number
        else: 
            merged_list.append(right[j])
            j = j + 1 #same as for i case
    
    # Appends the last item 
    #one becomes exhausted
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list

        
        

def merge_sort(arr: list) -> list: 
    """
    len of the list, divide by two, divides elements into two, do recursion, and compare when len is 1, then work back. 
    """

    if len(arr) <=1: 
        return arr #one element and hence sorted
    mid = len(arr) // 2 
    left = arr[:mid] 
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)