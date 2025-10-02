#%%
import time
import matplotlib.pyplot as plt
from sorting import bubble_sort, merge_sort
from numpy.random import randint
from precision import Precision as p

bubble_time = []
merge_time = []
list_length = []

def plotting(number, interval):
    for n in range(number):
        list = [p(randint(-100,100)) for i in range(0,n)] 
        b_ts = time.time()
        bs_list = bubble_sort(list)
        b_te = time.time()
        b_tot = b_te - b_ts
        bubble_time.append(b_tot)

        m_ts = time.time()
        ms_list = merge_sort(list)
        m_te = time.time()
        m_tot = m_te - m_ts
        merge_time.append(m_tot)
        
        list_length.append(n)
        n += interval
    plt.figure()
    plt.plot(list_length, bubble_time, label="Bubble Sort Time")
    plt.plot(list_length, merge_time, label="Merge Sort Time")
    plt.xlabel("List Lengths")
    plt.ylabel("Time Elapsed")
    plt.title("Compare")
    plt.legend()
    plt.tight_layout()
    plt.show()

# %%
