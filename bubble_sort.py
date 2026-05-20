import time

def bubble_sort(sort_list: list):

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



def improved_bubble_sort(sort_list: list, n1=0, n2=1) -> list:

    list_length = len(sort_list)
    list_index = list_length -1

    #if we have not reached the end of the list yet
    if n2 >= list_index:

        #if number on right is bigger than left
        if sort_list[n2] < sort_list[n1]:

            first_number = sort_list[n1]
            second_number = sort_list[n2]

            #swap
            sort_list[n1] = second_number
            sort_list[n2] = first_number

    else:
        return sort_list

    return bubble_sort(sort_list, n1+1, n2+1)

    #loop is done when orig_list[n+1] gives error and no swaps were made



