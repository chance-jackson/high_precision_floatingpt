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
