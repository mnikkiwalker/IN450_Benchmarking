import time

def partition(arr, l, h):
    i = l - 1
    pivot = arr[h]

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

"""
GeeksforGeeks. (2025, November 7). Python program for iterative quick sort. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-program-for-iterative-quick-sort/
"""


def quicksort(arr, l=0):
    h = len(arr)-1
    size = h - l + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

"""
GeeksforGeeks. (2025, November 7). Python program for iterative quick sort. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-program-for-iterative-quick-sort/
"""


def quicksort_run(array):
  
  start = time.time()

  quicksort(array)

  end = time.time()
  duration = end-start
  return array, duration



