from precision import Precision as p
from numpy.random import randint
import time
import matplotlib.pyplot as plt
import numpy as np

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

N = np.arange(10,100000,1000)
execution_time_bubble = []
for n in range(len(N)):
    A = [p(randint(-100,100)) for i in range(0,n)] #list of random numbers between -100, 100, converted to our high precision data type

    tic = time.time()
    out = bubble_sort(A)
    toc = time.time()

    execution_time_bubble.append(toc-tic)

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

execution_time_merge = []
for n in range(len(N)):
    A = [p(randint(-100,100)) for i in range(0,n)] #list of random numbers between -100, 100, converted to our high precision data type
    
    tic = time.time()
    out = merge_sort(A)
    toc = time.time()

    execution_time_merge.append(toc-tic)

plt.plot(N,execution_time_bubble,label="Bubble Sort")
plt.plot(N,execution_time_merge,label="Merge Sort")
plt.xlabel("Number of Elements in List")
plt.ylabel("Execution Time")
plt.title("Time Complexity Comparison Between Merge and Bubble Sort")
plt.legend(loc = "upper left")
#plt.xscale("log")
#plt.yscale("log")
plt.savefig("timecomplexity.png",dpi=300)

#print([str(out[i]) for i in range(len(A))]) #print out string representations

