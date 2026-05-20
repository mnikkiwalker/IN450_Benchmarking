import generate_list as gd
import bubble_sort



small_list = gd.generate_list(100)

#original list
print()
print("Original List")
print("-"*20)
for i, number in enumerate(small_list):
    print(i+1," - ",number)


#sort list
small_list, small_list_duration = bubble_sort.bubble_sort(small_list)
duration_ms = format(small_list_duration * 1000, ".0f")
print()
print("Sorted List duration: ", duration_ms, "ms")
print("-"*20)
for i, number in enumerate(small_list):
    print(i+1," - ",number)