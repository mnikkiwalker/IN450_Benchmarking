import time

def loop_bubble_sort(sort_list: list):

    start = time.time()
    
    n = len(sort_list)
    list_index = n-1

    #for each number in each position (n-1 for position instead of len)
    for i in range(list_index):

        #for each remaining number in the list
        for j in range(list_index - i):

            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]

    end = time.time()
    duration = end-start

    return sort_list, duration

"""
W3Schools.com. (n.d.). https://www.w3schools.com/python/python_dsa_bubblesort.asp
"""




def recursive_bubble_sort(sort_list, is_sorted=None, step=0, start=None):

    if not start:
        start = time.time()

    if step is 1 or is_sorted:
        end = time.time()
        duration = end-start
        # base case: l_elems is already sorted or we pass through the list len(l_elems) times
        return sort_list, duration
    
    else:
        is_swapped = False
        for i in range(len(sort_list) - 1):
            # compares each pair of adjacent items and swaps them if they are in the wrong order
            if sort_list[i] > sort_list[i + 1]:
                is_swapped = True
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
        # if is_swapped is True, the algorithm needs to pass through the list again
        return recursive_bubble_sort(sort_list, not is_swapped, step - 1, start)


"""
jootse84. (n.d.). Bubble sort recursive implementation in Python. Gist. https://gist.github.com/jootse84/3c51a776471a37beebac10d42ba9f42f
"""


